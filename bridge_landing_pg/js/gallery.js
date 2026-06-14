/* ── MODELS ── */
const MODELS = [
  {
    name: 'Alexis Ocean', age: 24, location: '3 miles away',
    status: 'Online now', lastActive: '2 min ago',
    bio: '"Fitness trainer by day, trouble at night 😈 I match energy — bring yours."',
    tags: ['fitness', 'travel', 'night owl'],
    photoCount: 247, videoCount: 48,
    message: 'Hey, I saw your profile and honestly? You seem like exactly my type 🔥',
    type: 'athletic', skin: 'white',
    photos: ['images/alexis1.jpg', 'images/alexis2.jpg', 'images/alexis3.jpg', 'images/alexis4.jpg'],
  },
  {
    name: 'Alisha Bell', age: 27, location: '1 mile away',
    status: 'Online now', lastActive: '5 min ago',
    bio: '"Artist & overthinker. Here for a good time, not a long time 🎨 Surprise me."',
    tags: ['art', 'music', 'wine lover'],
    photoCount: 183, videoCount: 31,
    message: "I don't usually message first but something about your profile caught my eye...",
    type: 'petite', skin: 'latina',
    photos: ['images/alisha1.jpg', 'images/alisha2.jpg', 'images/alisha3.jpg', 'images/alisha4.jpg'],
  },
  {
    name: 'Amber Xoo', age: 22, location: '5 miles away',
    status: 'Live now 🔴', lastActive: 'Live now',
    bio: '"Full-time bad influence 🌶️ Part-time angel. Always online late. Come find out why."',
    tags: ['gaming', 'cosplay', 'late nights'],
    photoCount: 312, videoCount: 67,
    message: 'You seem like exactly my type tbh... should we find out? 😏',
    type: 'curvy', skin: 'mixed',
    photos: ['images/amber1.jpg', 'images/amber2.jpg', 'images/amber3.jpg', 'images/amber4.jpg'],
  },
  {
    name: 'Cali Moon', age: 29, location: '8 miles away',
    status: 'Online now', lastActive: '12 min ago',
    bio: '"Beach girl, sun & secrets ☀️ More fun than my bio suggests. Way more."',
    tags: ['beach', 'yoga', 'foodie'],
    photoCount: 198, videoCount: 44,
    message: 'Okay so I may have looked at your profile more than once 😅',
    type: 'athletic', skin: 'white',
    photos: ['images/cali1.jpg', 'images/cali2.jpg', 'images/cali3.jpg', 'images/cali4.jpg'],
  },
  {
    name: 'Anastasia', age: 26, location: '2 miles away',
    status: 'Online now', lastActive: '8 min ago',
    bio: '"Eastern European mystery 🖤 I speak fluent trouble. Curious? You should be."',
    tags: ['fashion', 'travel', 'dancing'],
    photoCount: 276, videoCount: 59,
    message: 'We have 3 things in common already. Curious which ones? 🔒',
    type: 'exotic', skin: 'white',
    photos: ['images/anastasia1.jpg', 'images/anastasia2.jpg', 'images/anastasia3.jpg', 'images/anastasia4.jpg'],
  },
  {
    name: 'April Wong', age: 23, location: '4 miles away',
    status: 'Live now 🔴', lastActive: 'Live now',
    bio: '"Soft aesthetic, hard to forget 🌸 Your new favourite distraction. Don\'t say I didn\'t warn you."',
    tags: ['k-pop', 'skincare', 'cats'],
    photoCount: 341, videoCount: 72,
    message: 'Not gonna lie, I swiped right immediately 💕 ping me?',
    type: 'petite', skin: 'asian',
    photos: ['images/april1.jpg', 'images/april2.jpg', 'images/april3.jpg', 'images/april4.jpg'],
  },
  {
    name: 'Eva Williams', age: 31, location: '6 miles away',
    status: 'Online now', lastActive: '19 min ago',
    bio: '"Confident. Curious. Slightly chaotic 🔥 You\'ve been warned. Still here? Perfect."',
    tags: ['fitness', 'red wine', 'hiking'],
    photoCount: 229, videoCount: 38,
    message: "Your profile is actually interesting. That's rare here 👀",
    type: 'curvy', skin: 'black',
    photos: ['images/eva1.jpg', 'images/eva2.jpg', 'images/eva3.jpg', 'images/eva4.jpg'],
  },
  {
    name: 'Maya Levi', age: 28, location: '7 miles away',
    status: 'Live now 🔴', lastActive: 'Live now',
    bio: '"Leo energy — can\'t help it 🦁 Not here to be boring. Match me if you dare."',
    tags: ['astrology', 'photography', 'spontaneous'],
    photoCount: 194, videoCount: 55,
    message: "Tell me something about yourself that your friends don't know 🔥",
    type: 'exotic', skin: 'latina',
    photos: ['images/maya1.jpg', 'images/maya2.jpg', 'images/maya3.jpg', 'images/maya4.jpg'],
  },
];

const FREE_VIEWS = 3;

const CLIPS = [
  { src: 'videos/cali_01.mp4',      free: true  },
  { src: 'videos/alisha_01.mp4',    free: true  },
  { src: 'videos/amber_01.mp4',     free: true  },
  { src: 'videos/mia_01.mp4',       free: true  },
  { src: 'videos/gia_01.mp4',       free: false },
  { src: 'videos/olivia_01.mp4',    free: false },
  { src: 'videos/eva_01.mp4',       free: false },
  { src: 'videos/anastasia_01.mp4', free: false },
];

/* ── SIDE PANEL ── */
const PANEL_PHOTOS = [
  { src: 'images/alexis1.jpg',    live: true,  locked: false },
  { src: 'images/alisha1.jpg',    live: false, locked: false },
  { src: 'images/amber1.jpg',     live: true,  locked: false },
  { src: 'images/cali1.jpg',      live: false, locked: false },
  { src: 'images/anastasia1.jpg', live: false, locked: true  },
  { src: 'images/april1.jpg',     live: true,  locked: false },
  { src: 'images/eva1.jpg',       live: false, locked: true  },
  { src: 'images/maya1.jpg',      live: false, locked: false },
  { src: 'images/alexis2.jpg',    live: false, locked: true  },
  { src: 'images/alisha2.jpg',    live: true,  locked: false },
  { src: 'images/amber2.jpg',     live: false, locked: true  },
  { src: 'images/cali2.jpg',      live: false, locked: true  },
];

function buildSidePanel() {
  const mosaic = document.getElementById('spMosaic');
  if (!mosaic) return;

  mosaic.innerHTML = PANEL_PHOTOS.map(p => `
    <div class="sp-tile${p.locked ? ' sp-tile--locked' : ''}" onclick="aff('side_tile')">
      <img src="${p.src}" alt="" loading="lazy">
      ${p.live   ? '<span class="sp-live-badge">LIVE</span>' : ''}
      ${p.locked ? '<div class="sp-lock">🔒</div>' : ''}
    </div>`).join('');

  // Rotate featured model card every 8s
  let fi = 0;
  function updateFeatured() {
    const m      = MODELS[fi % MODELS.length];
    const isLive = m.status.includes('Live');
    const bio    = m.bio.replace(/"/g, '').slice(0, 58) + '…';
    document.getElementById('spFeatured').innerHTML = `
      <div class="sp-featured-card" onclick="aff('side_featured')">
        <img class="sp-feat-img" src="${m.photos[0]}" alt="${m.name}">
        <div>
          <div class="sp-feat-name">
            ${m.name}, ${m.age}
            ${isLive ? '<span class="sp-feat-live">● LIVE</span>' : ''}
          </div>
          <div class="sp-feat-loc">📍 ${m.location}</div>
          <div class="sp-feat-bio">${bio}</div>
        </div>
      </div>`;
    fi++;
  }
  updateFeatured();
  setInterval(updateFeatured, 8000);
}

/* ── MATCH % ── */
function calcMatch(model) {
  if (!prefType && !prefSkin) return 72 + Math.floor(Math.random() * 22);
  let score = 62;
  if (prefType && (prefType === 'any' || prefType === model.type)) score += 25;
  else if (prefType) score += Math.floor(Math.random() * 8);
  if (prefSkin && (prefSkin === 'any' || prefSkin === model.skin)) score += 18;
  else if (prefSkin) score += Math.floor(Math.random() * 5);
  score += Math.floor(Math.random() * 10) - 4;
  return Math.min(99, Math.max(68, score));
}

/* ── BUILD GALLERY ── */
function buildGallery() {
  const body = document.getElementById('galBody');

  let html = `
    <div class="gal-header">
      <h2>Your <em>matches</em> are here</h2>
      <p>Based on your preferences — ${matchTotal || 247} compatible profiles found</p>
    </div>
    <div class="clips-section">
      <div class="clips-label">Live Clips</div>
      <div class="clips-scroll">`;

  CLIPS.forEach(c => {
    if (c.free) {
      html += `<div class="clip-card" onclick="playClip(this)">
        <video muted loop playsinline preload="metadata"><source src="${c.src}" type="video/mp4"></video>
        <div class="clip-overlay"><div class="clip-play">▶</div></div>
      </div>`;
    } else {
      html += `<div class="clip-card locked" onclick="aff('clip_lock')">
        <video muted loop playsinline preload="metadata"><source src="${c.src}" type="video/mp4"></video>
        <div class="clip-overlay"><div class="clip-play">🔒</div></div>
      </div>`;
    }
  });

  html += `</div></div>`;

  MODELS.forEach((m, mi) => {
    const locked   = mi >= FREE_VIEWS;
    const isLive   = m.status.includes('Live');
    const ringClass = isLive ? 'ring-live' : 'ring-online';
    const matchPct  = calcMatch(m);
    const endMs     = isLive ? Date.now() + (18 + Math.floor(Math.random() * 22)) * 60000 : 0;

    html += `<div class="model-card ${locked ? 'locked-card' : 'free-card'}" id="mrow${mi}">`;

    html += `<div class="mc-head">
      <div class="mc-avatar-wrap ${ringClass}">
        <img class="mc-avatar" src="${m.photos[0]}" alt="${m.name}">
        <div class="mc-notif">1</div>
      </div>
      <div class="mc-head-info">
        <div class="mc-name">${m.name}, <span class="mc-age">${m.age}</span></div>
        <div class="mc-loc">📍 ${m.location} · ${m.lastActive}</div>
        ${isLive ? `<div class="mc-live-row">
          <div class="mc-live-dot"></div>
          <span class="mc-countdown" data-end="${endMs}">Going offline soon…</span>
        </div>` : ''}
      </div>
      <div class="mc-match-box">
        <div class="mc-match-pct">${matchPct}%</div>
        <div class="mc-match-lbl">match</div>
      </div>
    </div>`;

    html += `<div class="mc-bio">${m.bio}</div>`;
    html += `<div class="mc-tags">${m.tags.map(t => `<span class="mc-tag">${t}</span>`).join('')}</div>`;
    html += `<div class="mc-stats">
      <span>📸 ${m.photoCount} photos</span>
      <span>🎬 ${m.videoCount} videos</span>
    </div>`;

    if (locked) {
      html += `<div class="mc-message" onclick="aff('message_lock_${mi}')">
        <div class="mc-msg-avt"><img src="${m.photos[0]}" alt=""></div>
        <div class="mc-msg-body">
          <div class="mc-msg-text blurred">${m.message}</div>
          <span class="mc-msg-unlock">🔒 Unlock to read her message</span>
        </div>
        <div class="mc-msg-icon">💬</div>
      </div>`;
    } else {
      html += `<div class="mc-message">
        <div class="mc-msg-avt"><img src="${m.photos[0]}" alt=""></div>
        <div class="mc-msg-body">
          <div class="mc-msg-text">${m.message}</div>
          <span class="mc-msg-unlock" style="color:var(--dim)">Reply unlocked after sign-up ✓</span>
        </div>
        <div class="mc-msg-icon">💬</div>
      </div>`;
    }

    html += `<div class="photos-2col">`;
    m.photos.forEach((p, pi) => {
      if (locked) {
        html += `<div class="photo-thumb locked" onclick="aff('photo_lock_${mi}')">
          <img src="${p}" alt="" loading="lazy">
          <div class="lock-icon">🔒<span>Unlock</span></div>
        </div>`;
      } else {
        html += `<div class="photo-thumb" onclick="track('photo_view',{model:'${m.name}',idx:${pi}})">
          <img src="${p}" alt="" loading="lazy">
        </div>`;
      }
    });
    html += `</div>`;

    if (locked) {
      html += `<button class="mc-unlock-btn" onclick="aff('card_unlock_${mi}')">
        🔥 Unlock ${m.name.split(' ')[0]}'s Full Profile
      </button>`;
    }

    html += `</div>`;

    if (mi === FREE_VIEWS - 1) {
      html += `<div class="gal-lock-banner">
        <h3>🔒 ${MODELS.length - FREE_VIEWS} more profiles waiting</h3>
        <p>You've seen your free preview. Unlock all profiles, full galleries, and direct messaging now.</p>
        <button class="btn-main" style="width:100%" onclick="aff('banner_unlock')">Unlock All Profiles 🔥</button>
      </div>`;
    }
  });

  body.innerHTML = html;
  startCountdowns();
  initExitIntent();
}

/* ── COUNTDOWN TIMERS ── */
function startCountdowns() {
  setInterval(() => {
    document.querySelectorAll('.mc-countdown').forEach(el => {
      const end = parseInt(el.dataset.end);
      if (!end) return;
      const rem  = Math.max(0, end - Date.now());
      const mins = Math.floor(rem / 60000);
      const secs = Math.floor((rem % 60000) / 1000);
      el.textContent = rem === 0
        ? 'Going offline…'
        : `Going offline in ${mins}m ${secs}s`;
      if (rem === 0) el.style.color = '#f87171';
    });
  }, 1000);
}

/* ── CLIP PLAYBACK ── */
function playClip(card) {
  const vid     = card.querySelector('video');
  const overlay = card.querySelector('.clip-overlay');

  if (vid.paused) {
    document.querySelectorAll('.clip-card video').forEach(v => {
      if (v !== vid) {
        v.pause();
        v.closest('.clip-card').querySelector('.clip-overlay').style.opacity = '1';
      }
    });
    vid.play();
    overlay.style.opacity = '0';
  } else {
    vid.pause();
    overlay.style.opacity = '1';
  }
}

/* ── EXIT INTENT ── */
let exitShown    = false;
let exitInterval = null;

function initExitIntent() {
  document.addEventListener('mouseleave', e => {
    if (e.clientY < 20 && !exitShown) {
      exitShown = true;
      showExitModal();
    }
  });
}

function showExitModal() {
  document.getElementById('exitModal').classList.remove('off');
  let secs = 599;
  exitInterval = setInterval(() => {
    secs--;
    if (secs <= 0) { clearInterval(exitInterval); closeExit(); return; }
    const m = Math.floor(secs / 60).toString().padStart(2, '0');
    const s = (secs % 60).toString().padStart(2, '0');
    document.getElementById('exitTimerDisplay').textContent = `${m}:${s}`;
  }, 1000);
  track('exit_intent_shown');
}

function closeExit() {
  clearInterval(exitInterval);
  document.getElementById('exitModal').classList.add('off');
}

/* ── LEGAL MODALS ── */
function openLegal(type) {
  document.getElementById(type === 'terms' ? 'termsModal' : 'privacyModal').classList.remove('off');
}

function closeLegal(type) {
  document.getElementById(type === 'terms' ? 'termsModal' : 'privacyModal').classList.add('off');
}

/* ── INIT ── */
document.addEventListener('DOMContentLoaded', buildSidePanel);
