# How to Use the WordPress Plugin

## What This Helps You Do

The Hi, Moose WordPress plugin lets you automatically convert your blog posts into engaging audio podcasts that visitors can listen to directly on your site. 

**Get the Hi, Moose plugin on WordPress.org** ➡️ <a href="https://wordpress.org/plugins/listen-to-this-article/" target="_blank">Listen to This Article - Text to Speech WordPress Plugin</a>

The **Listen to This Article** plugin integrates with Hi, Moose's Podcast Generator to:

- **Transform written content into conversational audio** - Two AI voices discuss your article naturally
- **Embed audio players automatically** - Players appear on your posts with your branding
- **Improve accessibility** - Give readers an audio option for consuming content
- **Increase engagement** - Keep visitors on your site longer with audio content
- **Support 24+ languages** - Generate podcasts in multiple languages

Unlike standalone text-to-speech tools, this creates natural, conversational podcasts where two AI hosts discuss your content—making it more engaging than robotic narration.

---

## When to Use This

- **Blog-heavy WordPress sites** - Convert articles into audio automatically
- **Content marketing** - Give your audience multiple ways to consume content
- **Accessibility improvement** - Make content available to audio-first audiences
- **Engagement boost** - Increase time-on-site metrics
- **Multilingual sites** - Create audio versions in various languages
- **News and updates** - Let busy readers listen on-the-go
- **Educational content** - Provide audio learning alternatives

---

## Before You Start

### Requirements

1. **WordPress Installation**

   - WordPress 6.0 or higher
   - PHP 7.4 or higher
   - Active WordPress site with admin access

2. **Hi, Moose Account**

   - Free or paid Hi, Moose subscription
   - Domain configured in Hi, Moose settings
   - Access to Podcast Generator feature

3. **Plugin Installation**

   - Ability to install plugins on your WordPress site
   - Plugins permission (Administrator role)

### Important Notes

- The plugin currently supports the **Podcast Generator** feature only
- Audio files are hosted by Hi, Moose (not on your WordPress server) and use a global CDN
- Your domain must be whitelisted in Hi, Moose to play audio
- If you're on the Free or BYOK plan, each podcast generation uses podcast generation credits
- For Paid plans, each podcast generation uses AI tokens

---

## Step-by-Step Installation

### 1. Install the Plugin

#### Method A: From WordPress.org (Recommended)

1. **Log in to your WordPress admin dashboard**
   - Navigate to your WordPress site's admin area (typically `yoursite.com/wp-admin`)

2. **Go to Plugins → Add New**
   - Click **Plugins** in the left sidebar
   - Click **Add New** at the top

3. **Search for the plugin**
   - In the search box, type: `Listen to This Article`
   - Look for the plugin by Hi, Moose (look for the dog logo)

4. **Install the plugin**
   - Click **Install Now** button
   - Wait for installation to complete (usually 5-10 seconds)

5. **Activate the plugin**
   - Click **Activate** button
   - You'll be redirected to your Plugins page

#### Method B: Manual Upload

1. **Download the plugin**
   - Visit [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/)
   - Click the **Download** button
   - Save the `.zip` file to your computer

2. **Upload to WordPress**
   - Go to **Plugins → Add New** in WordPress admin
   - Click **Upload Plugin** at the top
   - Click **Choose File** and select the downloaded `.zip` file
   - Click **Install Now**

3. **Activate the plugin**
   - After installation, click **Activate Plugin**

---

## Configuring the Plugin

### 1. Set Your Domain in Hi, Moose

Before using the plugin, you must whitelist your domain in Hi, Moose:

1. **Log in to Hi, Moose** at [himoose.com](https://himoose.com)
2. **Go to Settings**
3. **Enter your WordPress domain** (e.g., `yoursite.com`)
4. **Save your settings**

**Why this matters**: Audio files will only play on whitelisted domains. When you generate a podcast in Hi, Moose, you'll see a "Domain Whitelisted" confirmation showing which domains can access the audio (e.g., "This audio file will only be accessible from himoose.com and himoose.com").

Without whitelisting, the audio player will not work on your WordPress site.

### 2. Access Plugin Settings

1. In WordPress admin, go to **Settings → Listen to This Article**
2. You'll see the plugin configuration page

### 3. Basic Configuration

The plugin works out-of-the-box with default settings, but you can customize:

- **Auto-embed**: Automatically add audio player to posts
- **Player position**: Anywhere within the body content
- **Player style**: Customize appearance to match your theme
- **Post types**: Which post types get audio (posts)

---

## Generating Podcasts

### For Individual Posts

#### Method 1: From the Post Editor

1. **Edit or create a post** in WordPress
2. **Look for the "Listen to This Article" meta box** in the sidebar
3. **Click "Generate Podcast"**
4. The plugin will:
   - Send your content to Hi, Moose
   - Generate the conversational audio
   - Automatically embed the player
5. **Preview the audio player** in your post

#### Method 2: From Post List

1. **Go to Posts → All Posts**
2. **Hover over any post**
3. **Click "Generate Podcast"** in the quick actions
4. Wait for generation to complete

### Bulk Generation

Generate podcasts for multiple posts at once:

1. **Go to Posts → All Posts**
2. **Select multiple posts** using checkboxes
3. **Choose "Generate Podcasts"** from Bulk Actions dropdown
4. **Click Apply**
5. Podcasts will be generated in the background

---

## Using the Audio Player

### Automatic Embedding

Once a podcast is generated:

- The audio player **automatically appears** in your post
- Position depends on your settings (top or bottom)
- Player includes:
  - Play/pause button
  - Progress bar
  - Playback speed controls
  - Volume control
  - Podcast title

### Manual Shortcode (Optional)

If you prefer manual placement, use the shortcode:

```
[himoose_podcast]
```

Insert this anywhere in your post content where you want the player to appear.

### Customizing Player Appearance

In **Settings → Listen to This Article**:

1. **Choose a color scheme** - Match your site's branding
2. **Select player size** - Compact, standard, or full-width
3. **Enable/disable controls** - Show or hide playback speed, download button, etc.
4. **Custom CSS** - Add your own styling if needed

---

## Managing Podcasts

### Regenerate a Podcast

If you update your post content:

1. **Edit the post** in WordPress
2. **Find the "Listen to This Article" meta box**
3. **Click "Regenerate Podcast"**
4. The plugin will create a new audio version with updated content

### Delete a Podcast

To remove the audio from a post:

1. **Edit the post**
2. **Click "Delete Podcast"** in the meta box
3. The audio player will be removed from the post

### View Podcast Statistics

See how many people are listening:

1. **Go to Settings → Listen to This Article**
2. **Click the "Analytics" tab**
3. View metrics:
   - Total plays
   - Average listen time
   - Most popular posts
   - Completion rates

---

## Troubleshooting

### Plugin Issues

**Audio player not showing:**

- Verify domain is set in Hi, Moose settings
- Check that post has a generated podcast
- Clear WordPress cache
- Check for JavaScript conflicts with other plugins

**"Domain not whitelisted" error:**

- Go to Hi, Moose settings
- Add your WordPress domain (without http:// or https://)
- Save and try again

**Generation fails:**

- Check your Hi, Moose account has available credits (if on a Free or BYOK plan)
- Verify post has sufficient content (minimum 800 words recommended)
- Ensure post is published and publicly accessible
- Check Hi, Moose API connection within the WordPress Settings

**Player not styled correctly:**

- Check for theme CSS conflicts
- Try disabling other audio/media plugins temporarily
- Clear browser cache
- Use custom CSS in plugin settings

### WordPress Compatibility

**Theme conflicts:**

- Most themes work out-of-the-box
- If issues occur, try switching to a default WordPress theme temporarily
- Contact support with your theme name

**Page builder compatibility:**

- Works with: Gutenberg, Classic Editor, Elementor, Divi
- May need manual shortcode placement with some builders

**Caching plugins:**

- Clear cache after generating podcasts
- Exclude audio player elements from caching if issues persist

---

## Advanced Features

### Custom Voice Selection

Hi, Moose's Podcast Generator uses two AI voices for natural conversation:

**Host Voice**: The primary narrator who introduces topics and asks questions
**Guest Voice**: The secondary voice who provides answers and additional context

Available voices include options with different tones and personalities.

To customize voices:

1. **Go to Hi, Moose Podcast Generator** at himoose.com
2. **Select your preferred Host and Guest voices** from the dropdowns
3. **Generate the podcast** with your voice pairing
4. **Copy the audio embed code** and use it in WordPress

### Advanced Conversation Customization

For more control over how the podcast sounds, Hi, Moose offers advanced customization options:

**Podcast Length**:

- Choose from: Short (4-5 minutes), Medium, or Long
- Longer content = more detailed discussion
- Shorter = focused on key takeaways

**Conversation Guidance** (all optional):

- **Host Direction**: Guide how the host should present (e.g., "friendly, confident, and curious")
- **Guest Direction**: Direct the guest's style (e.g., "analytical, detail-oriented, but still friendly")
- **The Scene**: Set the environment (e.g., "a quiet podcast studio that is warm")
- **Conversation Style**: Overall tone (e.g., "warm", "professional", "casual")
- **Conversation Pace**: Speed of dialogue (e.g., "medium", "fast", "slow")
- **Accent**: Voice accent preference (e.g., "neutral US")
- **More Context**: Additional instructions for the conversation (e.g., "the listener is a busy marketer who wants key takeaways on engagement, SEO and AEO")

These advanced options are available when you generate podcasts directly in Hi, Moose. The WordPress plugin uses default settings but you can customize individual podcasts in the Hi, Moose dashboard.

### Language Support

Generate podcasts in different languages:

**Auto-detection (Recommended)**: Hi, Moose automatically detects your article's language and generates audio to match. This is the default and works for 24+ languages.

**Manual selection**: If needed, you can manually select a language in Hi, Moose's Podcast Generator:

1. **Go to Podcast Generator** at himoose.com
2. **Select Language** from the dropdown (instead of "Auto-detect from article")
3. **Generate podcast** - AI will speak in the selected language

Supported languages include:
- English, Spanish, French, German, Italian, Portuguese
- Chinese, Japanese, Korean
- Arabic, Hindi, Dutch, Polish, Russian
- And 12+ more languages

### Custom Player Branding

Customize the audio player's appearance to match your brand:

**Player Colors**:

1. **Primary Color**: Main player controls and progress bar color
2. **Secondary Color (Gradient)**: Gradient accent for visual depth
3. Use the color pickers in Hi, Moose Podcast Generator to match your brand

**Player Title**:

- Toggle "Show title above player" to display/hide the article title
- Helps users identify what they're listening to

**Preview**: Hi, Moose shows a live preview of your player as you customize it

These settings apply to each podcast individually. You can choose different settings per podcast if you prefer.

---

## Best Practices

### Content Optimization

**Ideal post length:**

- 800-3000 words works best
- Shorter content feels rushed
- Longer content should be split into series

### User Experience

**Player placement:**

- Place at the **top** for maximum visibility
- Place at **bottom** if you want readers to see other content first

**Call-to-action:**

- Add a custom title on the audio player: "Prefer to listen? Click play below!"
- Encourage audio consumption in your intro
- Mention podcast availability in social shares

### Performance

**Generation timing:**

- Don't generate for very short posts (< 500 words)
- Update podcasts only when content significantly changes

---

## Plugin Settings Reference

### General Settings

- **Enable plugin**: Turn podcast generation on/off site-wide
- **Auto-embed**: Automatically add players to the top of the post body. The *himoose_podcast* shortcode will override this.

---

## Related Hi, Moose Features

### Podcast Generator

The WordPress plugin uses Hi, Moose's Podcast Generator:

- **Direct control**: Generate and customize in Hi, Moose dashboard
- **More options**: Advanced voice selection, tone adjustment
- **Embed codes**: Get custom embed code for copy/paste placement

See the [Podcast Generator](../features/podcast-generator.md) documentation for full feature details.

---

## Support & Resources

### Getting Help

**Plugin issues:**

- Check WordPress.org plugin support forum
- Search common issues in FAQ section
- Contact Hi, Moose support

**Feature requests:**

- Submit ideas on [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/)
- Vote on existing feature requests
- Join Hi, Moose community discussions

**Hi, Moose account issues:**

- Email support@himoose.com
- Verify subscription and credits

### Useful Links

- **Listen to this Article - Text to Speech WordPress Plugin page**: [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/)
- **Hi, Moose dashboard**: [himoose.com/dashboard](https://himoose.com/dashboard)
- **Podcast Generator docs**: [Podcast Generator](../features/podcast-generator.md)

---

## FAQ

**Q: Does this work with Gutenberg?**  
A: Yes! The plugin works with Gutenberg (Block Editor), Classic Editor, and most page builders.

**Q: Are audio files hosted on my server?**  
A: No, audio is hosted by Hi, Moose. This saves your server storage and bandwidth.

**Q: Does this affect my site speed?**  
A: No, audio is loaded on-demand and the player size is minimal. 

**Q: How much does it cost?**  
A: The WordPress plugin is **free**. Podcast generation uses AI tokens, or podcast generation credits if you're on the Free or BYOK plans.

---

**Ready to make your content even more engaging?** Install the plugin from [WordPress.org](https://wordpress.org/plugins/listen-to-this-article/) and start generating podcasts.
