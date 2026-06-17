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

    if (request.method === 'POST' && url.pathname === '/register') {
      return handleHoticaRegister(request, env, corsHeaders);
    }

    return new Response('Not found', { status: 404 });
  }
};

async function handleAwProfiles(request, env, corsHeaders) {
  if (!env.ADULTWORK_API_KEY) {
    return new Response(JSON.stringify({ error: 'API not configured' }), {
      status: 503, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  const url = new URL(request.url);
  const awParams = new URLSearchParams({
    ProfilesPerPage: url.searchParams.get('limit') || '24',
    PageNumber: url.searchParams.get('page') || '1',
    OrderBy: url.searchParams.get('orderBy') || 'lastupdated',
    IsWebcam: 'true',
    GenderIDs: url.searchParams.get('genderIds') || '1',
  });

  const awBase = env.ADULTWORK_API_BASE || 'https://api.adultwork.com';
  let awRes;
  try {
    awRes = await fetch(`${awBase}/v1/Search/SearchProfiles?${awParams}`, {
      headers: {
        'X-ApiKey': env.ADULTWORK_API_KEY,
        'X-ApiSecret': env.ADULTWORK_API_SECRET || '',
        'Accept': 'application/json',
        'X-CaseType': 'camelcase',
      },
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
  const pid = env.ADULTWORK_PID || '';

  const profiles = (data.profiles || data.searchResults || [])
    .filter(p => p.userId && p.profileImageUrl)
    .map(p => {
      const profileUrl = `https://m.adultwork.com/${p.userId}`;
      const referralUrl = pid
        ? `https://refer.adultwork.com/?PID=${pid}&T=${encodeURIComponent(profileUrl)}`
        : profileUrl;
      return {
        userId: p.userId,
        nickname: p.nickname || '',
        thumbnail: p.profileImageUrl,
        isOnline: p.isLoggedInNow || false,
        rating: p.rating || null,
        location: p.location || '',
        referralUrl,
      };
    });

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
