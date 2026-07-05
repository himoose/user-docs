// Override logo link to point to homepage
// This runs immediately to ensure search engines see the correct link
(function() {
    // Get homepage URL from meta tag
    var homepageUrl = document.querySelector('meta[name="homepage-url"]')?.content || 'https://himoose.com';
    
    // Function to update logo link
    function updateLogoLink() {
        var logoLink = document.querySelector('a[data-slot="button"][href*="himoose.com/docs/"]');
        if (logoLink && logoLink.href !== homepageUrl) {
            logoLink.href = homepageUrl;
            logoLink.title = 'Go to Hi, Moose home page';
            return true;
        }
        return false;
    }
    
    // Try to update immediately
    if (!updateLogoLink()) {
        // If not found, observe DOM for when it's added
        var observer = new MutationObserver(function(mutations, obs) {
            if (updateLogoLink()) {
                obs.disconnect();
            }
        });
        observer.observe(document.documentElement, {
            childList: true,
            subtree: true
        });
    }
})();

// Scroll the left-hand nav so the current page's highlighted link starts
// near the top of the visible nav area, instead of always loading with
// "Home" at the top and leaving the active link buried further down for
// pages that live lower in a long nav tree. Each page is a full navigation
// (no client-side router), so this needs to run on every load.
(function () {
    function scrollActiveNavItemIntoView() {
        var container = document.querySelector('[data-slot="sidebar-content"]');
        if (!container) {
            return;
        }

        var active = container.querySelector('a[data-active="true"]');
        if (!active) {
            return;
        }

        var topBreathingRoom = 24;
        var containerRect = container.getBoundingClientRect();
        var activeRect = active.getBoundingClientRect();
        var delta = (activeRect.top - containerRect.top) - topBreathingRoom;

        if (delta > 0) {
            container.scrollTop += delta;
        }
    }

    function runOnNextFrame() {
        window.requestAnimationFrame(scrollActiveNavItemIntoView);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runOnNextFrame);
    } else {
        runOnNextFrame();
    }
})();
