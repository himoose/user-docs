// Privacy-light PostHog capture for the docs site. Hand-rolled on
// purpose: the full posthog-js bundle drags in feature flags, surveys and
// replay we will never use here, and a ~2 KB client keeps the site's
// progressive-enhancement posture (plain pages work identically with this
// blocked, failed, or JS off).
//
// Same PostHog project as the desktop app (public write-only token), so web
// pageviews, download clicks and in-app first-runs land in one dashboard.
//
// Privacy posture, by construction:
//  - No cookies. The visitor id lives in sessionStorage, so it dies with the
//    tab and a returning visitor counts as new. That is the trade we chose to
//    stay banner-free.
//  - $process_person_profile:false — events stay anonymous, no person
//    profiles are ever created for web visitors.
//  - Do Not Track / Global Privacy Control disable everything.
//  - Only pageviews and download clicks are sent. No autocapture, no input
//    or content scraping of any kind.
//
// This is a copy of the marketing site's script (marketing-site/src/assets/
// js/analytics.js) with site:'docs' — keep the two in sync when editing.
(function () {
  try {
    var TOKEN = 'phc_BhDU7TyEbHAjyCapZWwxM7qwSDEqgwA7qD6HnHTFR9KN';
    var ENDPOINT = 'https://eu.i.posthog.com/i/v0/e/';
    var SITE = 'docs';

    if (navigator.doNotTrack === '1' || window.doNotTrack === '1' ||
        navigator.globalPrivacyControl === true) {
      return;
    }

    function uuid() {
      if (window.crypto && crypto.randomUUID) return crypto.randomUUID();
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (Math.random() * 16) | 0;
        return (c === 'x' ? r : (r & 0x3) | 0x8).toString(16);
      });
    }

    // UUIDv7 (millisecond timestamp prefix) — PostHog requires this format
    // for $session_id; a v4 id here is rejected and the event loses its
    // session, which is what feeds the built-in Web Analytics dashboard.
    function uuidv7() {
      var ts = Date.now().toString(16).padStart(12, '0');
      var rand = '';
      for (var i = 0; i < 20; i++) rand += ((Math.random() * 16) | 0).toString(16);
      return ts.slice(0, 8) + '-' + ts.slice(8, 12) + '-7' + rand.slice(0, 3) +
        '-' + (((Math.random() * 4) | 0) + 8).toString(16) + rand.slice(3, 6) +
        '-' + rand.slice(6, 18);
    }

    function sessionValue(key, make) {
      try {
        var v = sessionStorage.getItem(key);
        if (!v) {
          v = make();
          sessionStorage.setItem(key, v);
        }
        return v;
      } catch (e) {
        return make(); // storage blocked: per-pageview ids, still counted
      }
    }

    var distinctId = sessionValue('hm_aid', uuid);
    var sessionId = sessionValue('hm_sid', uuidv7);

    function baseProperties() {
      var props = {
        $session_id: sessionId,
        $current_url: location.href,
        $pathname: location.pathname,
        $host: location.host,
        $referrer: document.referrer || '$direct',
        $referring_domain: '$direct',
        $screen_width: window.screen ? screen.width : undefined,
        $screen_height: window.screen ? screen.height : undefined,
        // Anonymous events only: never create a person profile from the web.
        $process_person_profile: false,
        site: SITE,
        page_lang: document.documentElement.getAttribute('lang') || 'en'
      };
      if (document.referrer) {
        try {
          props.$referring_domain = new URL(document.referrer).hostname;
        } catch (e) { /* unparsable referrer stays $direct */ }
      }
      try {
        var params = new URLSearchParams(location.search);
        ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'ref']
          .forEach(function (key) {
            var value = params.get(key);
            if (value) props[key] = value.slice(0, 200);
          });
      } catch (e) { /* no query params is the common case */ }
      return props;
    }

    function capture(event, properties) {
      var payload = {
        api_key: TOKEN,
        event: event,
        distinct_id: distinctId,
        timestamp: new Date().toISOString(),
        properties: baseProperties()
      };
      if (properties) {
        for (var key in properties) payload.properties[key] = properties[key];
      }
      // text/plain keeps this a CORS simple request (no preflight), and
      // keepalive lets a download-click event outlive the navigation.
      fetch(ENDPOINT, {
        method: 'POST',
        keepalive: true,
        headers: { 'Content-Type': 'text/plain' },
        body: JSON.stringify(payload)
      }).catch(function () { /* analytics is best-effort */ });
    }

    capture('$pageview');

    // Download clicks: same anchors the install-claim script watches. The os
    // buckets mirror install-claim.js so the two data sets line up.
    document.addEventListener('click', function (event) {
      try {
        var anchor = event.target && event.target.closest
          ? event.target.closest('a[href*="/downloads/"]')
          : null;
        if (!anchor) return;
        var href = anchor.getAttribute('href') || '';
        var idx = href.indexOf('/downloads/');
        if (idx === -1) return;
        var path = href.slice(idx);
        var os = 'other';
        if (path.indexOf('/downloads/windows') === 0) os = 'windows';
        else if (path.indexOf('/downloads/mac') === 0) os = 'mac';
        capture('download_clicked', { os: os, download_path: path });
      } catch (e) { /* never interfere with the download click */ }
    });
  } catch (e) {
    // Never break the site over analytics.
  }
})();
