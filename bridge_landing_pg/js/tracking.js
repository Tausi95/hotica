/* ── AFFILIATE & UTM ── */

const BASE_LINK = 'https://www.rkj3s1ks.com/4784JN/2CTPL/';

function getUTM() {
  const p = new URLSearchParams(window.location.search);
  const keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'sub1', 'sub2'];
  return keys.reduce((acc, k) => {
    if (p.get(k)) acc[k] = p.get(k);
    return acc;
  }, {});
}

function buildAffLink() {
  const params = new URLSearchParams(getUTM()).toString();
  return BASE_LINK + (params ? '?' + params : '');
}

function track(eventName, props) {
  const payload = props || {};
  if (typeof gtag !== 'undefined')  gtag('event', eventName, payload);
  if (typeof fbq  !== 'undefined')  fbq('trackCustom', eventName, payload);
}

function aff(label) {
  track('affiliate_click', { label, source: getUTM().utm_source || 'direct' });
  window.open(buildAffLink(), '_blank', 'noopener');
}
