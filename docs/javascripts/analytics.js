// Privacy-light PostHog capture for the docs site. Hand-rolled on
// purpose: the full posthog-js bundle drags in feature flags, surveys and
// replay we will never use here, and a ~4 KB client keeps the site's
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
//  - The user-agent string is passed through as $raw_user_agent. It is a
//    header every request already sends; PostHog needs it on the event to
//    classify the visit as a real browser rather than unidentified
//    automation. No new information leaves the browser.
//  - Pageviews, scroll progress, link clicks and download clicks only. No
//    autocapture, no input or content scraping of any kind.
//
// This is a copy of the marketing site's script (marketing-site/src/assets/
// js/analytics.js) with site:'docs' — keep the two in sync when editing.
(function () {
  try {
    var TOKEN = 'phc_BhDU7TyEbHAjyCapZWwxM7qwSDEqgwA7qD6HnHTFR9KN';
    var ENDPOINT = 'https://r.himoose.com/i/v0/e/';
    var SITE = 'docs';

    if (navigator.doNotTrack === '1' || window.doNotTrack === '1' ||
        navigator.globalPrivacyControl === true) {
      return;
    }

    // Personal opt-out, for keeping our own browsing out of the numbers.
    // PostHog discards client IPs for this project, so there is no IP to
    // filter on at the other end; the exclusion has to happen here. Visit
    // any page with ?hm_track=off once per browser to stop sending, and
    // ?hm_track=on to start again. Survives across sessions on purpose.
    var OPT_OUT_KEY = 'hm_track_off';
    try {
      var trackParam = new URLSearchParams(location.search).get('hm_track');
      if (trackParam === 'off') localStorage.setItem(OPT_OUT_KEY, '1');
      else if (trackParam === 'on') localStorage.removeItem(OPT_OUT_KEY);
      if (localStorage.getItem(OPT_OUT_KEY) === '1') return;
    } catch (e) { /* storage blocked: nothing opted out, carry on */ }

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

    // First-touch campaign, remembered for the session. The utm query string
    // only exists on the landing URL, so an ad visitor who clicks through to a
    // second page stops looking like paid traffic from that click onward. The
    // per-URL utm_* properties below are left exactly as they were; these are
    // separate, sticky, and safe to group by across a whole visit.
    var CAMPAIGN_KEY = 'hm_campaign';
    var CAMPAIGN_FIELDS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'ref'];
    var campaign = {};
    try {
      var landing = {};
      var landingParams = new URLSearchParams(location.search);
      CAMPAIGN_FIELDS.forEach(function (key) {
        var value = landingParams.get(key);
        if (value) landing[key] = value.slice(0, 200);
      });
      if (Object.keys(landing).length) {
        campaign = landing;
        sessionStorage.setItem(CAMPAIGN_KEY, JSON.stringify(landing));
      } else {
        campaign = JSON.parse(sessionStorage.getItem(CAMPAIGN_KEY) || '{}') || {};
      }
    } catch (e) { /* storage blocked or unparsable: this visit stays untagged */ }

    // Device, browser and OS. posthog-js would derive these client-side; we
    // do the same parse ourselves, using PostHog's own value spellings so the
    // Web Analytics device/browser tiles read them.
    var ua = navigator.userAgent || '';

    function deviceType() {
      if (/iPad/i.test(ua)) return 'Tablet';
      // iPadOS 13+ claims to be a Mac; touch points give it away.
      if (/Macintosh/i.test(ua) && navigator.maxTouchPoints > 1) return 'Tablet';
      if (/Android/i.test(ua) && !/Mobile/i.test(ua)) return 'Tablet';
      if (/Tablet|PlayBook|Silk|Kindle/i.test(ua)) return 'Tablet';
      if (/Mobi|iPhone|iPod|Android|BlackBerry|IEMobile|Opera Mini/i.test(ua)) return 'Mobile';
      return 'Desktop';
    }

    function browserName() {
      if (/Edg\//i.test(ua)) return 'Microsoft Edge';
      if (/OPR\/|Opera/i.test(ua)) return 'Opera';
      if (/SamsungBrowser/i.test(ua)) return 'Samsung Internet';
      if (/Firefox\/|FxiOS/i.test(ua)) return 'Firefox';
      if (/Chrome\/|CriOS/i.test(ua)) return 'Chrome';
      if (/Safari\//i.test(ua)) return 'Safari';
      return 'Other';
    }

    function osName() {
      if (/Windows/i.test(ua)) return 'Windows';
      if (/iPhone|iPad|iPod/i.test(ua)) return 'iOS';
      if (/Android/i.test(ua)) return 'Android';
      if (/CrOS/i.test(ua)) return 'Chrome OS';
      if (/Macintosh|Mac OS X/i.test(ua)) return 'Mac OS X';
      if (/Linux/i.test(ua)) return 'Linux';
      return 'Other';
    }

    var device = deviceType();

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
        $viewport_width: window.innerWidth,
        $viewport_height: window.innerHeight,
        $device_type: device,
        $browser: browserName(),
        $os: osName(),
        $raw_user_agent: ua.slice(0, 500),
        // Anonymous events only: never create a person profile from the web.
        $process_person_profile: false,
        site: SITE,
        page_lang: document.documentElement.getAttribute('lang') || 'en',
        campaign_source: campaign.utm_source || '(untagged)',
        campaign_medium: campaign.utm_medium,
        campaign_name: campaign.utm_campaign,
        campaign_ref: campaign.ref
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

    // Page scripts (e.g. for-agencies.js) emit their own events through this.
    // It is absent when tracking is off, so callers must feature-check it.
    window.hmTrack = capture;

    capture('$pageview');

    /* ---------- how far down the page they get ---------- */

    // Sections are opt-in: any element carrying data-section is a checkpoint,
    // counted as reached once its top passes the middle of the viewport. A
    // page with no data-section attributes still reports scroll percentages.
    var sections = [].slice.call(document.querySelectorAll('[data-section]'));
    var maxSectionIndex = -1;
    var maxSectionName = null;

    if (sections.length && window.IntersectionObserver) {
      var observer = new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (!entries[i].isIntersecting) continue;
          var index = sections.indexOf(entries[i].target);
          if (index > maxSectionIndex) {
            maxSectionIndex = index;
            maxSectionName = entries[i].target.getAttribute('data-section');
          }
        }
      }, { rootMargin: '0px 0px -50% 0px', threshold: 0 });
      sections.forEach(function (section) { observer.observe(section); });
    }

    var MILESTONES = [25, 50, 75, 90, 100];
    var nextMilestone = 0;
    var maxScroll = 0;
    var startedAt = Date.now();
    var clicked = false;
    var ticking = false;

    function pageHeight() {
      var body = document.body || {};
      var el = document.documentElement || {};
      return Math.max(body.scrollHeight || 0, body.offsetHeight || 0,
        el.clientHeight || 0, el.scrollHeight || 0, el.offsetHeight || 0);
    }

    function scrollable() {
      return pageHeight() - window.innerHeight > 80;
    }

    function measureScroll() {
      var total = pageHeight();
      if (total <= 0) return;
      var seen = (window.pageYOffset || document.documentElement.scrollTop || 0) +
        window.innerHeight;
      var percent = Math.min(100, Math.round((seen / total) * 100));
      if (percent > maxScroll) maxScroll = percent;

      // A page that fits on one screen is "100% scrolled" the moment it
      // loads. Firing five milestones for that is noise, so milestones are
      // only for pages long enough to actually scroll.
      if (!scrollable()) return;
      while (nextMilestone < MILESTONES.length && maxScroll >= MILESTONES[nextMilestone]) {
        capture('scroll_depth', {
          depth: MILESTONES[nextMilestone],
          seconds_to_reach: Math.round((Date.now() - startedAt) / 1000),
          section: maxSectionName || undefined
        });
        nextMilestone++;
      }
    }

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        ticking = false;
        measureScroll();
      });
    }, { passive: true });
    window.addEventListener('resize', measureScroll, { passive: true });
    measureScroll();

    // One summary per pageview, on the first time the page is hidden. This is
    // best-effort by nature (a killed tab may never report), which is why the
    // scroll_depth milestones above are sent as they happen rather than being
    // rolled into this event.
    //
    // A link opened in a background tab is hidden from the start and may be
    // closed without ever being looked at. Reporting that as a 0% exit would
    // drag the drop-off numbers down with visits that never happened, so a
    // page that was never visible reports nothing.
    var exitSent = false;
    var wasVisible = document.visibilityState !== 'hidden';
    function sendExit() {
      if (exitSent || !wasVisible) return;
      exitSent = true;
      measureScroll();
      capture('page_exit', {
        max_scroll_percent: maxScroll,
        max_section: maxSectionName || 'none',
        max_section_index: maxSectionIndex,
        sections_on_page: sections.length,
        seconds_on_page: Math.round((Date.now() - startedAt) / 1000),
        page_scrollable: scrollable(),
        clicked_something: clicked
      });
    }

    document.addEventListener('visibilitychange', function () {
      if (document.visibilityState === 'hidden') {
        sendExit();
        return;
      }
      wasVisible = true;
      // requestAnimationFrame is paused while a tab is hidden, so the scroll
      // handler can be left mid-flight; clear it on the way back in.
      ticking = false;
      measureScroll();
    });
    window.addEventListener('pagehide', sendExit);

    /* ---------- where they go next ---------- */

    function sectionOf(node) {
      var host = node.closest ? node.closest('[data-section]') : null;
      return host ? host.getAttribute('data-section') : undefined;
    }

    document.addEventListener('click', function (event) {
      try {
        var anchor = event.target && event.target.closest
          ? event.target.closest('a[href]')
          : null;
        if (!anchor) return;
        var href = anchor.getAttribute('href') || '';
        clicked = true;

        // Download clicks keep their own event so the existing install funnel
        // and the os buckets in install-claim.js stay untouched.
        var idx = href.indexOf('/downloads/');
        if (idx !== -1) {
          var path = href.slice(idx);
          var os = 'other';
          if (path.indexOf('/downloads/windows') === 0) os = 'windows';
          else if (path.indexOf('/downloads/mac') === 0) os = 'mac';
          capture('download_clicked', {
            os: os,
            download_path: path,
            section: sectionOf(anchor)
          });
          return;
        }

        // Everything else: internal links show onward navigation, and
        // off-site links (the console sign-up, above all) never produce a
        // pageview here, so a click is the only place they can be counted.
        var target;
        try {
          target = new URL(anchor.href, location.href);
        } catch (e) {
          return;
        }
        if (target.protocol !== 'http:' && target.protocol !== 'https:') return;

        capture('link_click', {
          to_host: target.host,
          to_path: target.pathname,
          is_external: target.host !== location.host,
          is_anchor: target.hash && target.pathname === location.pathname ? true : false,
          section: sectionOf(anchor),
          link_text: (anchor.textContent || '').trim().slice(0, 60),
          max_scroll_percent: maxScroll
        });
      } catch (e) { /* never interfere with the click */ }
    });
  } catch (e) {
    // Never break the site over analytics.
  }
})();
