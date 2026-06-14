/* ── QUIZ STATE ── */
let userAge   = null;
let meetWho   = null;
let prefType  = null;
let prefSkin  = null;
let matchTotal = 0;

/* ── NAVIGATION ── */
function go(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.add('off'));
  document.getElementById(id).classList.remove('off');

  const pageMap = {
    p1: 'gate', p2: 'your_age', p3: 'who_meet',
    p4: 'type', p5: 'appearance', p7: 'loading',
    p8: 'email', p9: 'verify', pgal: 'gallery',
  };
  if (pageMap[id]) track('page_view', { page_title: pageMap[id] });
}

/* ── ONLINE COUNTER ── */
let onlineBase = 3204;

function fluctuateOnline() {
  onlineBase += Math.floor(Math.random() * 40) - 18;
  onlineBase  = Math.max(2900, Math.min(3650, onlineBase));
  document.querySelectorAll('.online-count').forEach(el => {
    el.textContent = onlineBase.toLocaleString() + ' online now';
  });
}
setInterval(fluctuateOnline, 45000);

/* ── AGE OPTIONS ── */
const AGE_OPTS = [
  { val: '18–24', lbl: 'Young Adult' },
  { val: '25–34', lbl: 'Mid Twenties' },
  { val: '35–44', lbl: 'Thirties' },
  { val: '45–54', lbl: 'Forties' },
  { val: '55+',   lbl: 'Fifty Plus' },
  { val: 'Any',   lbl: 'No Preference' },
];

function buildAgeGrid(gridId, btnId, varName) {
  document.getElementById(gridId).innerHTML = AGE_OPTS.map(o => `
    <div class="age-opt" onclick="pickAge(this,'${gridId}','${btnId}','${varName}','${o.val}')">
      <div class="age-val">${o.val}</div>
      <div class="age-lbl">${o.lbl}</div>
    </div>`).join('');
}

function pickAge(el, gridId, btnId, varName, val) {
  document.querySelectorAll(`#${gridId} .age-opt`).forEach(e => e.classList.remove('sel'));
  el.classList.add('sel');
  if (varName === 'userAge') userAge = val;
  document.getElementById(btnId).disabled = false;
}

/* ── WHO TO MEET ── */
const MEET_OPTS = [
  { key: 'women', photo: 'images/april1.jpg', lbl: 'Women' },
  { key: 'men',   photo: null,                lbl: 'Men' },
  { key: 'both',  photo: null,                lbl: 'Both' },
];

function buildMeetGrid() {
  document.getElementById('meetGrid').innerHTML = MEET_OPTS.map(o => `
    <div class="meet-card" onclick="pickMeet(this,'${o.key}')">
      <div class="meet-photo-wrap">${
        o.photo
          ? `<img class="meet-photo" src="${o.photo}" alt="${o.lbl}">
             <div class="meet-photo-overlay"></div>`
          : `<div class="meet-ph-gradient meet-ph-${o.key}">
               <div class="meet-ph-icon">${o.key === 'men' ? '♂' : '♀♂'}</div>
             </div>
             <div class="meet-photo-overlay"></div>`
      }</div>
      <div class="meet-lbl">${o.lbl}</div>
    </div>`).join('');
}

function pickMeet(el, val) {
  document.querySelectorAll('.meet-card').forEach(e => e.classList.remove('sel'));
  el.classList.add('sel');
  meetWho = val;
  document.getElementById('btnMeet').disabled = false;
}

/* ── TYPE PREFERENCE ── */
const TYPE_OPTS = [
  { key: 'petite',   photo: 'images/alisha1.jpg',    lbl: 'Petite' },
  { key: 'curvy',    photo: 'images/amber1.jpg',     lbl: 'Curvy' },
  { key: 'athletic', photo: 'images/alexis1.jpg',    lbl: 'Athletic' },
  { key: 'exotic',   photo: 'images/anastasia1.jpg', lbl: 'Exotic' },
  { key: 'milf',     photo: 'images/eva1.jpg',       lbl: 'MILF' },
  { key: 'any',      photo: 'images/cali1.jpg',      lbl: 'Any Type' },
];

function buildTypeGrid() {
  document.getElementById('typeGrid').innerHTML = TYPE_OPTS.map(o => `
    <div class="type-opt" onclick="pickType(this,'${o.key}')">
      <div class="type-photo-wrap">
        <img class="type-photo" src="${o.photo}" alt="${o.lbl}">
        <div class="type-photo-overlay"></div>
      </div>
      <div class="type-lbl">${o.lbl}</div>
    </div>`).join('');
}

function pickType(el, val) {
  document.querySelectorAll('.type-opt').forEach(e => e.classList.remove('sel'));
  el.classList.add('sel');
  prefType = val;
  document.getElementById('btnType').disabled = false;
}

/* ── APPEARANCE ── */
const SKIN_OPTS = [
  { key: 'any',    lbl: 'Any',       photo: 'images/maya1.jpg' },
  { key: 'white',  lbl: 'Caucasian', photo: 'images/cali1.jpg' },
  { key: 'latina', lbl: 'Latina',    photo: 'images/alisha1.jpg' },
  { key: 'black',  lbl: 'Black',     photo: 'images/eva1.jpg' },
  { key: 'asian',  lbl: 'Asian',     photo: 'images/april1.jpg' },
  { key: 'mixed',  lbl: 'Mixed',     photo: 'images/amber1.jpg' },
];

function buildSkinGrid() {
  document.getElementById('skinGrid').innerHTML = SKIN_OPTS.map(o => `
    <div class="skin-opt" onclick="pickSkin(this,'${o.key}')">
      <div class="skin-photo-wrap">
        <img class="skin-photo" src="${o.photo}" alt="${o.lbl}">
        <div class="skin-photo-overlay"></div>
      </div>
      <div class="skin-lbl">${o.lbl}</div>
    </div>`).join('');
}

function pickSkin(el, val) {
  document.querySelectorAll('.skin-opt').forEach(e => e.classList.remove('sel'));
  el.classList.add('sel');
  prefSkin = val;
  document.getElementById('btnSkin').disabled = false;
}

/* ── LOADING SCREEN ── */
function startLoading() {
  go('p7');
  matchTotal = 180 + Math.floor(Math.random() * 140);

  const msgs = [
    'Scanning profiles in your area…',
    'Filtering by your preferences…',
    'Checking who\'s online right now…',
    'Almost ready…',
  ];

  let mi = 0, count = 0, prog = 0;
  const fillEl   = document.getElementById('loadFill');
  const numEl    = document.getElementById('loadNum');
  const statusEl = document.getElementById('loadStatus');

  const msgInt   = setInterval(() => { mi = (mi + 1) % msgs.length; statusEl.textContent = msgs[mi]; }, 900);
  const countInt = setInterval(() => {
    count = Math.min(count + Math.ceil(matchTotal / 36), matchTotal);
    prog  = Math.min(prog  + 100 / 36, 100);
    numEl.textContent   = count.toLocaleString();
    fillEl.style.width  = prog + '%';

    if (count >= matchTotal) {
      clearInterval(countInt);
      clearInterval(msgInt);
      statusEl.textContent = 'Found your matches! 🎉';
      document.getElementById('matchDisp').textContent = matchTotal.toLocaleString();
      setTimeout(() => go('p8'), 1100);
    }
  }, 65);
}

/* ── HELPERS ── */
function generateUsername(email) {
  const base = email.split('@')[0].replace(/[^a-zA-Z0-9]/g, '').toLowerCase().slice(0, 12);
  return base + Math.floor(1000 + Math.random() * 9000);
}

function generatePassword() {
  const u = 'ABCDEFGHJKMNPQRSTUVWXYZ';
  const l = 'abcdefghjkmnpqrstuvwxyz';
  const n = '23456789';
  const s = '!@#$';
  const all = u + l + n;
  let pw = u[Math.floor(Math.random() * u.length)]
         + l[Math.floor(Math.random() * l.length)]
         + n[Math.floor(Math.random() * n.length)]
         + s[Math.floor(Math.random() * s.length)];
  for (let i = 0; i < 8; i++) pw += all[Math.floor(Math.random() * all.length)];
  return pw.split('').sort(() => Math.random() - 0.5).join('');
}

function onTurnstileSuccess(token) { window._tsToken = token; }

/* ── EMAIL SUBMIT ── */
async function submitEmail() {
  const inp = document.getElementById('emailInp');
  const val = inp.value.trim();

  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
    inp.style.borderColor = 'var(--pink2)';
    inp.focus();
    return;
  }

  inp.style.borderColor = '';
  track('email_submitted', { domain: val.split('@')[1], source: getUTM().utm_source || 'direct' });

  try {
    await fetch('https://hv-api.chancy-tsonga.workers.dev/register', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email:    val,
        username: generateUsername(val),
        password: generatePassword(),
        turnstileToken: window._tsToken,
        prefs:  { age: userAge, meets: meetWho, type: prefType, skin: prefSkin },
        source: getUTM(),
        ts:     Date.now(),
      }),
    });
  } catch (_) { /* fail silently — navigation always proceeds */ }

  go('p9');
  runVerify();
}

/* ── VERIFICATION ANIMATION ── */
function runVerify() {
  const steps = [
    { dotId: 'vd1', txtId: 'vt1', stepId: 'vs1', done: 'Email verified ✓' },
    { dotId: 'vd2', txtId: 'vt2', stepId: 'vs2', done: 'Preferences matched ✓' },
    { dotId: 'vd3', txtId: 'vt3', stepId: 'vs3', done: 'Matches loaded ✓' },
  ];

  let si = 0;

  function advance() {
    if (si >= steps.length) {
      setTimeout(() => { buildGallery(); go('pgal'); }, 600);
      return;
    }
    const s = steps[si];
    document.getElementById(s.stepId).classList.remove('active');
    document.getElementById(s.stepId).classList.add('done');
    document.getElementById(s.dotId).innerHTML = '✓';
    document.getElementById(s.txtId).textContent = s.done;
    si++;

    if (si < steps.length) {
      const ns = steps[si];
      document.getElementById(ns.stepId).classList.add('active');
      document.getElementById(ns.dotId).innerHTML = '<div class="vring"></div>';
    }
    setTimeout(advance, 1300);
  }
  setTimeout(advance, 1500);
}

/* ── INIT ── */
buildAgeGrid('yourAgeGrid', 'btnYourAge', 'userAge');
buildMeetGrid();
buildTypeGrid();
buildSkinGrid();
