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
