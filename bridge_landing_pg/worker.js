export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    const corsHeaders = {
      'Access-Control-Allow-Origin': env.ALLOWED_ORIGIN || '',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    if (request.method === 'GET' && url.pathname === '/api/aw-profiles') {
      return handleAwProfiles(request, env, corsHeaders);
    }


    const profileApiMatch = url.pathname.match(/^\/api\/aw-profile\/([^/]+)$/);
    if (request.method === 'GET' && profileApiMatch) {
      return handleAwProfileApi(profileApiMatch[1], env, corsHeaders);
    }

    const profilePageMatch = url.pathname.match(/^\/profiles\/([^/]+?)\/?$/);
    if (request.method === 'GET' && profilePageMatch) {
      return handleProfilePage(profilePageMatch[1], request, env);
    }

    if (request.method === 'GET' && url.pathname === '/api/news') {
      return handleNews(request, corsHeaders);
    }

    if (request.method === 'POST' && url.pathname === '/register') {
      return handleHoticaRegister(request, env, corsHeaders);
    }

    return new Response('Not found', { status: 404 });
  }
};

// ── AW helpers ────────────────────────────────────────────────────────────────

function awHeaders(env) {
  return {
    'X-ApiKey': env.ADULTWORK_API_KEY,
    'X-ApiSecret': env.ADULTWORK_API_SECRET || '',
    'Accept': 'application/json',
    'X-CaseType': 'camelcase',
    'x-internal-secret': env.AW_INTERNAL_SECRET || '',
  };
}

async function fetchAwProfile(userId, env) {
  const awBase = env.ADULTWORK_API_BASE || 'https://developers.adultwork.com';

  // Try the single-profile endpoint first
  const profileRes = await fetch(`${awBase}/v1/Profile/${userId}`, {
    headers: awHeaders(env),
  }).catch(() => null);

  if (profileRes && profileRes.ok) {
    const data = await profileRes.json();
    return normaliseProfile(data, env);
  }

  // Fall back to SearchProfiles with a UserId filter
  const params = new URLSearchParams({
    ProfilesPerPage: '1',
    PageNumber: '1',
    UserId: userId,
  });
  const searchRes = await fetch(`${awBase}/v1/Search/SearchProfiles?${params}`, {
    headers: awHeaders(env),
  }).catch(() => null);

  if (!searchRes || !searchRes.ok) return null;

  const data = await searchRes.json();
  const p = (data.profiles || data.searchResults || [])[0];
  return p ? normaliseProfile(p, env) : null;
}

function normaliseProfile(p, env) {
  const rawThumb = p.profileThumbnailURL || p.profileImageUrl || p.thumbnailUrl || '';
  const thumbnail = rawThumb.startsWith('//') ? 'https:' + rawThumb : rawThumb;

  const pid = env.ADULTWORK_PID || '';
  const fallbackUrl = `https://www.adultwork.com/${p.userID || p.userId || p.id}`;
  const referralUrl = p.profileURL ||
    (pid ? `https://refer.adultwork.com/?PID=${pid}&T=${encodeURIComponent(fallbackUrl)}` : fallbackUrl);

  return {
    userId:     String(p.userID || p.userId || p.id || ''),
    nickname:   p.nickname || p.username || '',
    thumbnail,
    isOnline:   p.availableTodayEscort || p.availableNowWebcam || p.isLoggedInNow || false,
    rating:     p.ratings?.ratings ?? p.ratings?.total ?? p.rating ?? null,
    location:   p.town || p.region || p.country || p.location || '',
    bio:        p.summary || p.aboutMe || p.description || '',
    age:        p.age || null,
    referralUrl,
  };
}

// ── Route handlers ─────────────────────────────────────────────────────────────

async function handleAwProfiles(request, env, corsHeaders) {
  if (!env.ADULTWORK_API_KEY) {
    return new Response(JSON.stringify({ error: 'API not configured' }), {
      status: 503, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const url = new URL(request.url);
  const awParams = new URLSearchParams({
    ProfilesPerPage: url.searchParams.get('limit') || '24',
    PageNumber:      url.searchParams.get('page') || '1',
    OrderBy:         url.searchParams.get('orderBy') || 'lastupdated',
    GenderIDs:       url.searchParams.get('genderIds') || '1',
  });

  const awBase = env.ADULTWORK_API_BASE || 'https://developers.adultwork.com';
  let awRes;
  try {
    awRes = await fetch(`${awBase}/v1/Search/SearchProfiles?${awParams}`, {
      headers: awHeaders(env),
    });
  } catch {
    return new Response(JSON.stringify({ error: 'AdultWork API unreachable' }), {
      status: 502, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  if (!awRes.ok) {
    return new Response(JSON.stringify({ error: 'AdultWork API error', status: awRes.status }), {
      status: awRes.status, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const data = await awRes.json();
  const profiles = (data.profiles || data.searchResults || [])
    .filter(p => (p.userID || p.userId) && (p.profileThumbnailURL || p.profileImageUrl))
    .map(p => normaliseProfile(p, env));

  return new Response(
    JSON.stringify({ profiles, total: data.totalResults || profiles.length }),
    {
      headers: {
        ...corsHeaders,
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=60',
      },
    }
  );
}

async function handleAwProfileApi(userId, env, corsHeaders) {
  if (!env.ADULTWORK_API_KEY) {
    return new Response(JSON.stringify({ error: 'API not configured' }), {
      status: 503, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const profile = await fetchAwProfile(userId, env);
  if (!profile) {
    return new Response(JSON.stringify({ error: 'Profile not found' }), {
      status: 404, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  return new Response(JSON.stringify(profile), {
    headers: {
      ...corsHeaders,
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=120',
    },
  });
}

async function handleProfilePage(slug, request, env) {
  if (!env.ADULTWORK_API_KEY) {
    return errorPage('Service unavailable', 503);
  }

  const profile = await fetchAwProfile(slug, env);
  if (!profile) {
    return errorPage('Profile not found', 404);
  }

  const html = renderProfileHtml(profile, new URL(request.url));

  return new Response(html, {
    headers: {
      'Content-Type': 'text/html;charset=UTF-8',
      'Cache-Control': 'public, max-age=120',
    },
  });
}

async function handleHoticaRegister(request, env, corsHeaders) {
  const corsHeaders2 = { ...corsHeaders, 'Access-Control-Allow-Methods': 'POST, OPTIONS' };

  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
      status: 400, headers: { ...corsHeaders2, 'Content-Type': 'application/json' }
    });
  }

  const { email, username, password, turnstileToken, hp = '' } = body;

  if (!email || !username || !password || !turnstileToken) {
    return new Response(JSON.stringify({ error: 'Missing required fields' }), {
      status: 400, headers: { ...corsHeaders2, 'Content-Type': 'application/json' }
    });
  }

  let hoticaRes;
  try {
    hoticaRes = await fetch('https://api.hotica.com/api/trpc/partner.register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-partner-id': env.PARTNER_ID,
        'x-partner-key': env.PARTNER_KEY,
        'Origin': env.ORIGIN_URL,
      },
      body: JSON.stringify({ username, email, password, turnstileToken, signupAsHost: false, hp }),
    });
  } catch {
    return new Response(JSON.stringify({ error: 'Upstream request failed' }), {
      status: 502, headers: { ...corsHeaders2, 'Content-Type': 'application/json' }
    });
  }

  const data = await hoticaRes.text();
  return new Response(data, {
    status: hoticaRes.status,
    headers: { ...corsHeaders2, 'Content-Type': 'application/json' },
  });
}

// ── News / RSS ────────────────────────────────────────────────────────────────

const RSS_FEEDS = {
  gossip: [
    'https://pagesix.com/feed/',
    'https://www.dailymail.co.uk/tvshowbiz/index.rss',
  ],
  crypto: [
    'https://cointelegraph.com/rss',
    'https://decrypt.co/feed',
  ],
  sports: [
    'https://feeds.bbci.co.uk/sport/football/rss.xml',
    'https://feeds.bbci.co.uk/sport/rss.xml',
  ],
  world: [
    'https://feeds.bbci.co.uk/news/world/rss.xml',
    'https://www.aljazeera.com/xml/rss/all.xml',
  ],
};

function extractImage(block) {
  // media:content or media:thumbnail — url attr in any position, single or double quotes
  let m = /(?:media:content|media:thumbnail)[^>]*\surl=["']([^"']+)["']/i.exec(block);
  if (m) return m[1];

  // enclosure tag — image type preferred but accept any
  m = /<enclosure[^>]*\surl=["']([^"']+)["'][^>]*(?:type=["']image[^"']*["'])?/i.exec(block);
  if (!m) m = /<enclosure[^>]*type=["']image[^"']*["'][^>]*\surl=["']([^"']+)["']/i.exec(block);
  if (m) return m[1];

  // img tag inside description/content CDATA
  m = /<img[^>]+src=["']([^"']+)["']/i.exec(block);
  if (m) return m[1];

  // bare image URL anywhere in block (jpg/jpeg/png/webp)
  m = /https?:\/\/[^\s"'<>]+\.(?:jpe?g|png|webp)(?:\?[^\s"'<>]*)?/i.exec(block);
  if (m) return m[0];

  return '';
}

function parseRss(xml) {
  const items = [];
  const itemRx = /<item[^>]*>([\s\S]*?)<\/item>/gi;
  let m;
  while ((m = itemRx.exec(xml)) !== null) {
    const block = m[1];
    const get = (tag) => {
      const r = new RegExp(`<${tag}[^>]*>(?:<!\\[CDATA\\[)?([\\s\\S]*?)(?:\\]\\]>)?<\\/${tag}>`, 'i');
      const match = r.exec(block);
      return match ? match[1].trim() : '';
    };
    const image = extractImage(block);

    const title = get('title');
    const link  = get('link') || (/<link[^>]*\/?>([^<]+)/i.exec(block) || [])[1] || '';
    if (!title || !link) continue;

    items.push({
      title:     title.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&#\d+;/g,'').slice(0,120),
      link:      link.trim(),
      image,
      summary:   get('description').replace(/<[^>]+>/g,'').replace(/&amp;/g,'&').slice(0,160),
      published: get('pubDate') || get('dc:date') || '',
      source:    '',
    });
    if (items.length >= 10) break;
  }
  return items;
}

async function fetchFeed(url) {
  try {
    const res = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; HoticaBot/1.0)' },
      cf: { cacheTtl: 600, cacheEverything: true },
    });
    if (!res.ok) return [];
    const xml = await res.text();
    const source = (/<title[^>]*>(?:<!\\[CDATA\\[)?([^<]{2,60})/i.exec(xml) || [])[1] || new URL(url).hostname;
    return parseRss(xml).map(a => ({ ...a, source: source.trim() }));
  } catch {
    return [];
  }
}

async function handleNews(request, corsHeaders) {
  const url = new URL(request.url);
  const category = url.searchParams.get('category') || 'world';
  const feeds = RSS_FEEDS[category] || RSS_FEEDS.world;

  const results = await Promise.all(feeds.map(fetchFeed));
  const articles = results.flat()
    .filter((a, i, arr) => arr.findIndex(b => b.title === a.title) === i)
    .slice(0, 20);

  return new Response(JSON.stringify({ category, articles }), {
    headers: {
      ...corsHeaders,
      'Content-Type': 'application/json',
      'Cache-Control': 'public, max-age=600',
    },
  });
}

// ── HTML rendering ─────────────────────────────────────────────────────────────

function esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function renderProfileHtml(p, pageUrl) {
  const title      = `${esc(p.nickname)} – Hotica`;
  const ogImage    = esc(p.thumbnail);
  const ogUrl      = esc(pageUrl.origin + pageUrl.pathname);
  const name       = esc(p.nickname || 'Profile');
  const location   = esc(p.location);
  const bio        = esc(p.bio || `${name} is online right now and waiting to connect with you.`);
  const ratingHtml = p.rating ? `★ ${Number(p.rating).toFixed(1)}` : '';
  const onlineText = p.isOnline ? '● Online now' : 'Recently active';
  const onlineCls  = p.isOnline ? 'id-online' : 'id-away';
  const ctaUrl     = esc(p.referralUrl);
  const ageStr     = p.age ? `${esc(String(p.age))} · ` : '';

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title}</title>
<meta property="og:title" content="${name} is waiting for you on Hotica">
<meta property="og:description" content="${bio.slice(0, 160)}">
<meta property="og:image" content="${ogImage}">
<meta property="og:url" content="${ogUrl}">
<meta property="og:type" content="profile">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${name} is waiting for you on Hotica">
<meta name="twitter:image" content="${ogImage}">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S8NPHZS7LL"></script>
<script>
window.dataLayer=window.dataLayer||[];
function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());
gtag('config','G-S8NPHZS7LL');
</script>
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:#1a1220;color:#fff;font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;overflow-x:hidden;}
:root{
  --navy:#1a1220;--card:#251c30;--card2:#2e2340;--border:#3d3055;
  --pink:#f080a0;--pink2:#e0506e;--glow:rgba(240,128,160,.32);
  --muted:#b0a0c0;--dim:#706080;
}
#ageGate{
  position:fixed;inset:0;z-index:300;background:rgba(18,12,26,.97);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:32px 24px;text-align:center;
}
#ageGate .ag-logo{font-size:1.8rem;font-weight:900;letter-spacing:-1px;margin-bottom:28px;}
#ageGate .ag-logo span{color:var(--pink);font-size:1.5em;line-height:.8;margin:0 -1px;}
.ag-photo{width:88px;height:88px;border-radius:50%;object-fit:cover;
  border:3px solid var(--pink);box-shadow:0 0 24px rgba(240,128,160,.4);margin-bottom:18px;}
.ag-h{font-size:1.5rem;font-weight:900;line-height:1.2;margin-bottom:8px;}
.ag-h em{font-style:normal;color:var(--pink);}
.ag-sub{font-size:.84rem;color:var(--muted);line-height:1.65;max-width:290px;margin-bottom:28px;}
.ag-btns{display:flex;flex-direction:column;gap:10px;width:100%;max-width:290px;}
.btn-main{border:none;cursor:pointer;font-weight:800;
  background:linear-gradient(135deg,var(--pink),var(--pink2));color:#fff;
  padding:16px 32px;border-radius:50px;font-size:1rem;letter-spacing:.3px;
  box-shadow:0 10px 28px var(--glow);transition:transform .2s,box-shadow .2s;width:100%;}
.btn-main:hover{transform:translateY(-2px);box-shadow:0 16px 36px var(--glow);}
.btn-ghost{border:1px solid var(--border);background:transparent;color:var(--muted);cursor:pointer;
  font-weight:700;padding:14px 32px;border-radius:50px;font-size:.9rem;
  transition:all .2s;width:100%;}
.btn-ghost:hover{border-color:var(--pink);color:var(--pink);}
.ag-legal{font-size:.63rem;color:var(--dim);max-width:290px;line-height:1.7;margin-top:14px;}
.ag-legal a{color:var(--muted);cursor:pointer;text-decoration:underline;}
.topbar{
  display:flex;align-items:center;justify-content:space-between;
  padding:12px 18px;position:sticky;top:0;z-index:10;
  background:rgba(26,18,32,.92);backdrop-filter:blur(18px);
  border-bottom:1px solid rgba(255,255,255,.05);
}
.logo{font-size:1.5rem;font-weight:900;letter-spacing:-1px;line-height:1;display:flex;align-items:center;}
.logo .o{color:var(--pink);font-size:1.3em;line-height:.8;margin:0 -1px;}
.back-btn{display:flex;align-items:center;gap:6px;color:var(--muted);font-size:.82rem;
  font-weight:600;text-decoration:none;padding:6px 10px;border-radius:20px;
  border:1px solid var(--border);background:rgba(255,255,255,.04);transition:all .2s;}
.back-btn:hover{border-color:var(--pink);color:var(--pink);}
.online-pill{display:flex;align-items:center;gap:6px;background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.07);padding:5px 12px;border-radius:20px;}
.dot{width:7px;height:7px;border-radius:50%;background:#4ade80;
  box-shadow:0 0 6px #4ade80;animation:blink 2s infinite;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:.3;}}
.online-pill span{font-size:.72rem;color:var(--muted);}
.hero{position:relative;width:100%;height:72vh;min-height:420px;overflow:hidden;}
.hero-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.hero-gradient{
  position:absolute;inset:0;
  background:linear-gradient(to bottom,
    rgba(26,18,32,.15) 0%,rgba(26,18,32,0) 30%,rgba(26,18,32,0) 55%,
    rgba(26,18,32,.85) 85%,rgba(26,18,32,1) 100%);
}
.hero-badge{
  position:absolute;top:14px;left:14px;display:flex;align-items:center;gap:6px;
  background:rgba(255,60,90,.18);border:1px solid rgba(255,60,90,.45);
  padding:5px 12px;border-radius:20px;font-size:.68rem;font-weight:800;color:#ff4060;
  letter-spacing:.08em;text-transform:uppercase;
}
.hero-badge .live-dot{width:6px;height:6px;border-radius:50%;background:#ff4060;
  box-shadow:0 0 6px #ff4060;animation:blink 1.4s infinite;}
.hero-bottom{position:absolute;bottom:0;left:0;right:0;padding:20px 20px 0;}
.profile-id{display:flex;align-items:flex-end;gap:14px;margin-bottom:0;}
.avatar-wrap{position:relative;flex-shrink:0;}
.avatar{width:74px;height:74px;border-radius:50%;object-fit:cover;
  border:3px solid var(--pink);box-shadow:0 0 20px rgba(240,128,160,.45);display:block;}
.avatar-badge{position:absolute;bottom:0;right:0;width:20px;height:20px;
  background:#4ade80;border:2px solid var(--navy);border-radius:50%;}
.id-text{flex:1;padding-bottom:6px;}
.id-name{font-size:1.55rem;font-weight:900;line-height:1.1;display:flex;align-items:center;gap:8px;}
.id-meta{font-size:.78rem;color:var(--muted);margin-top:3px;display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.sep{color:var(--dim);}
.id-online{color:#4ade80;font-weight:700;}
.id-away{color:var(--dim);font-weight:600;}
.rating-badge{font-size:.7rem;background:rgba(251,191,36,.12);border:1px solid rgba(251,191,36,.3);
  color:#fbbf24;border-radius:20px;padding:2px 8px;font-weight:700;}
.page{max-width:480px;margin:0 auto;padding:0 0 100px;}
.section{padding:22px 18px;}
.section+.section{border-top:1px solid rgba(255,255,255,.05);}
.sect-label{font-size:.62rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;
  color:var(--pink);margin-bottom:12px;display:flex;align-items:center;gap:7px;}
.sect-label::before{content:'';display:inline-block;width:14px;height:2px;background:var(--pink);border-radius:2px;}
.bio-text{font-size:.93rem;color:var(--muted);line-height:1.75;}
.msg-card{
  display:flex;align-items:center;gap:12px;
  background:rgba(240,128,160,.07);border:1px solid rgba(240,128,160,.22);
  border-radius:16px;padding:14px;cursor:pointer;transition:all .2s;text-decoration:none;
  display:flex;
}
.msg-card:hover{background:rgba(240,128,160,.12);border-color:rgba(240,128,160,.4);}
.msg-avatar{width:46px;height:46px;border-radius:50%;object-fit:cover;flex-shrink:0;
  border:2px solid rgba(240,128,160,.4);}
.msg-body{flex:1;min-width:0;}
.msg-sender{font-size:.78rem;font-weight:800;color:#fff;margin-bottom:3px;}
.msg-text{font-size:.82rem;color:var(--muted);filter:blur(5px);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;user-select:none;pointer-events:none;}
.msg-unlock{font-size:.68rem;color:var(--pink);font-weight:700;margin-top:3px;display:block;}
.msg-notif{width:20px;height:20px;background:#ef4444;border-radius:50%;
  font-size:.6rem;font-weight:900;color:#fff;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.cta-section{
  padding:20px 18px 28px;position:sticky;bottom:0;
  background:linear-gradient(to top,rgba(26,18,32,1) 80%,rgba(26,18,32,0));
  pointer-events:none;
}
.cta-inner{pointer-events:all;}
.cta-main{
  width:100%;padding:17px;border-radius:50px;border:none;
  background:linear-gradient(135deg,var(--pink),var(--pink2));color:#fff;
  font-size:1.05rem;font-weight:800;cursor:pointer;
  box-shadow:0 12px 32px var(--glow);transition:transform .2s,box-shadow .2s;
  display:flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;
}
.cta-main:hover{transform:translateY(-2px);box-shadow:0 18px 40px var(--glow);}
.cta-sub{
  width:100%;padding:13px;border-radius:50px;border:1px solid var(--border);
  background:rgba(255,255,255,.03);color:var(--muted);
  font-size:.88rem;font-weight:700;cursor:pointer;transition:all .2s;margin-top:9px;
  display:flex;align-items:center;justify-content:center;gap:7px;text-decoration:none;
}
.cta-sub:hover{border-color:var(--pink);color:var(--pink);}
.cta-pulse{display:flex;align-items:center;justify-content:center;gap:6px;
  font-size:.71rem;color:var(--dim);margin-top:9px;}
.cta-pulse .cpulse{width:6px;height:6px;border-radius:50%;background:#4ade80;
  box-shadow:0 0 5px #4ade80;animation:blink 1.8s infinite;}
.bg{position:fixed;inset:0;z-index:-1;overflow:hidden;pointer-events:none;}
.blob{position:absolute;border-radius:50%;filter:blur(120px);opacity:.1;}
.b1{width:500px;height:500px;background:var(--pink);top:-180px;left:-120px;animation:drift 12s ease-in-out infinite alternate;}
.b2{width:400px;height:400px;background:#8855cc;bottom:-100px;right:-80px;animation:drift 15s ease-in-out infinite alternate-reverse;}
@keyframes drift{from{transform:translate(0,0);}to{transform:translate(20px,16px)scale(1.08);}}
</style>
</head>
<body>
<div class="bg"><div class="blob b1"></div><div class="blob b2"></div></div>

<div id="ageGate">
  <div class="ag-logo">H<span>🔥</span>tica</div>
  <img class="ag-photo" src="${ogImage}" alt="${name}">
  <h2 class="ag-h"><em>${name}</em> wants<br>to connect with you</h2>
  <p class="ag-sub">She's online right now. This profile contains adult content — you must be 18 or older to continue.</p>
  <div class="ag-btns">
    <button class="btn-main" onclick="enterProfile()">Yes, I'm 18+ — Show Me 🔥</button>
    <button class="btn-ghost" onclick="window.location.href='about:blank'">No, I'm under 18</button>
  </div>
  <p class="ag-legal">By entering you confirm you are 18 or older and agree to our
    <a onclick="openLegal('terms')">Terms</a> and
    <a onclick="openLegal('privacy')">Privacy Policy</a>.</p>
</div>

<div class="topbar">
  <a class="back-btn" href="/browse/">← Browse</a>
  <div class="logo">H<span class="o">🔥</span>tica</div>
  <div class="online-pill"><div class="dot"></div><span id="onlineCount">3,204 online</span></div>
</div>

<div class="hero">
  <img class="hero-img" src="${ogImage}" alt="${name}">
  <div class="hero-gradient"></div>
  ${p.isOnline ? `<div class="hero-badge"><div class="live-dot"></div>Active now</div>` : ''}
  <div class="hero-bottom">
    <div class="profile-id">
      <div class="avatar-wrap">
        <img class="avatar" src="${ogImage}" alt="${name}">
        ${p.isOnline ? '<div class="avatar-badge"></div>' : ''}
      </div>
      <div class="id-text">
        <div class="id-name">${name} <span class="verified">✦</span>${ratingHtml ? `<span class="rating-badge">${ratingHtml}</span>` : ''}</div>
        <div class="id-meta">
          ${ageStr ? `<span>${ageStr.replace(' · ', '')}</span><span class="sep">·</span>` : ''}
          ${location ? `<span>${location}</span><span class="sep">·</span>` : ''}
          <span class="${onlineCls}">${onlineText}</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="page">
  <div class="section">
    <div class="sect-label">About Me</div>
    <p class="bio-text">${bio}</p>
  </div>

  <div class="section">
    <div class="sect-label">She Messaged You</div>
    <a class="msg-card" href="${ctaUrl}" target="_blank" rel="noopener noreferrer" onclick="track('message_preview')">
      <img class="msg-avatar" src="${ogImage}" alt="${name}">
      <div class="msg-body">
        <div class="msg-sender">${name}</div>
        <div class="msg-text">I think we'd have a lot to talk about. What do you say? 😊</div>
        <span class="msg-unlock">🔒 Tap to read &amp; reply</span>
      </div>
      <div class="msg-notif">1</div>
    </a>
  </div>
</div>

<div class="cta-section">
  <div class="cta-inner">
    <a class="cta-main" href="${ctaUrl}" target="_blank" rel="noopener noreferrer" onclick="track('cta_message')">
      💬 Message ${name} on Hotica
    </a>
    <a class="cta-sub" href="${ctaUrl}" target="_blank" rel="noopener noreferrer" onclick="track('cta_profile')">
      View Full Profile →
    </a>
    <div class="cta-pulse">
      <div class="cpulse"></div>
      ${p.isOnline ? 'She\'s online right now' : 'Check her profile on Hotica'}
    </div>
  </div>
</div>

<script>
function track(label){
  if(typeof gtag !== 'undefined') gtag('event','profile_click',{label,source:'aw_dynamic'});
}
function enterProfile(){
  track('age_confirmed');
  document.getElementById('ageGate').style.display='none';
}
let onlineBase=3204;
function fluctuateOnline(){
  onlineBase+=Math.floor(Math.random()*38)-17;
  onlineBase=Math.max(2900,Math.min(3600,onlineBase));
  const el=document.getElementById('onlineCount');
  if(el) el.textContent=onlineBase.toLocaleString()+' online';
}
setInterval(fluctuateOnline,42000);
function openLegal(type){
  alert(type==='terms'?'Adults only. You agree not to reproduce content without permission.':'We collect standard analytics only. No personal data on this page.');
}
</script>
</body>
</html>`;
}

function errorPage(message, status) {
  return new Response(`<!doctype html><html><head><meta charset=UTF-8><title>Hotica</title>
<style>body{background:#1a1220;color:#fff;font-family:system-ui;display:flex;align-items:center;justify-content:center;min-height:100vh;flex-direction:column;gap:16px;}
a{color:#f080a0;}</style></head>
<body><h2>${esc(message)}</h2><a href="/browse/">← Browse profiles</a></body></html>`,
    { status, headers: { 'Content-Type': 'text/html;charset=UTF-8' } }
  );
}
