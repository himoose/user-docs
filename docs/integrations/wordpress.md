# How to Use the WordPress Plugin

## What This Helps You Do

The Hi, Moose WordPress plugin lets you automatically convert your blog posts into engaging audio podcasts that visitors can listen to directly on your site. 

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

Best for sites publishing regular long-form content (800-3000 words per article).

---

## Before You Start

### Requirements

1. **WordPress Installation**
   - WordPress 5.0 or higher
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
- Audio files are hosted by Hi, Moose (not on your WordPress server)
- Your domain must be whitelisted in Hi, Moose to play audio
- Each podcast generation uses Hi, Moose credits based on your plan

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
   - Look for the plugin by Hi, Moose

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

Before using the plugin, configure your domain in Hi, Moose:

1. **Log in to Hi, Moose** at [himoose.com](https://himoose.com)
2. **Go to Settings**
3. **Enter your WordPress domain** (e.g., `yoursite.com`)
4. **Save your settings**

This whitelists your domain so audio files will play on your WordPress site.

### 2. Access Plugin Settings

1. In WordPress admin, go to **Settings → Listen to This Article**
2. You'll see the plugin configuration page

### 3. Basic Configuration

The plugin works out-of-the-box with default settings, but you can customize:

- **Auto-embed**: Automatically add audio player to posts
- **Player position**: Top or bottom of content
- **Player style**: Customize appearance to match your theme
- **Post types**: Which post types get audio (posts, pages, custom post types)

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
- Check your Hi, Moose account has available credits
- Verify post has sufficient content (minimum 800 words recommended)
- Ensure post is published and publicly accessible
- Check Hi, Moose API connection

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

Choose different AI voices for your podcasts:

1. **Go to Hi, Moose** website
2. **Generate a podcast** with your preferred voices
3. **Copy the audio ID**
4. **In WordPress**, use shortcode: `[himoose_podcast id="AUDIO_ID"]`

### Language Support

Generate podcasts in different languages:

1. **Ensure your post content is in the target language**
2. **In plugin settings**, select the language
3. **Generate podcast** - AI will speak in the selected language

Supported languages include:
- English, Spanish, French, German, Italian, Portuguese
- Chinese, Japanese, Korean
- Arabic, Hindi, Dutch, Polish, Russian
- And 12+ more languages

### Custom Branding

For paid Hi, Moose plans:

1. **Upload your logo** in plugin settings
2. **Set brand colors** to match your identity
3. **Customize player text** (e.g., "Listen to this post")
4. Audio players will reflect your branding

---

## Best Practices

### Content Optimization

**Ideal post length:**
- 800-3000 words works best
- Shorter content feels rushed
- Longer content should be split into series

**Content structure:**
- Use clear headings and sections
- Write conversationally (reads well when spoken)
- Avoid heavy jargon or complex formatting
- Include natural transitions between topics

### User Experience

**Player placement:**
- Place at the **top** for maximum visibility
- Place at **bottom** if you want readers to see content first
- Consider sticky/floating player for long posts

**Call-to-action:**
- Add a note: "Prefer to listen? Click play above!"
- Encourage audio consumption in your intro
- Mention podcast availability in social shares

### Performance

**Generation timing:**
- Generate podcasts during off-peak hours for bulk operations
- Don't generate for very short posts (< 500 words)
- Update podcasts only when content significantly changes

**Credit management:**
- Monitor your Hi, Moose usage in plugin analytics
- Prioritize podcast generation for high-traffic posts
- Consider which post types need audio (maybe not pages/archives)

---

## Plugin Settings Reference

### General Settings

- **Enable plugin**: Turn podcast generation on/off site-wide
- **Auto-embed**: Automatically add players to posts
- **Default position**: Where player appears (top/bottom)
- **Post types**: Which content types get podcasts

### Player Settings

- **Theme**: Light, dark, or auto (match system preference)
- **Size**: Compact, standard, or full-width
- **Controls**: Show/hide speed, volume, download, share
- **Color scheme**: Primary and accent colors

### Content Settings

- **Minimum word count**: Don't generate for short posts
- **Excluded categories**: Skip certain post categories
- **Content filter**: Remove specific elements (comments, ads, etc.)

### Advanced Settings

- **API settings**: Connection to Hi, Moose
- **Cache duration**: How long to cache audio files
- **Custom CSS**: Your own player styling
- **Debug mode**: Enable for troubleshooting

---

## Related Hi, Moose Features

### Podcast Generator

The WordPress plugin uses Hi, Moose's Podcast Generator:

- **Direct control**: Generate and customize in Hi, Moose dashboard
- **More options**: Advanced voice selection, tone adjustment
- **Embed codes**: Get custom embed codes for manual placement

See the [Podcast Generator](../features/podcast-generator.md) documentation for full feature details.

### Brand Voice

Customize how podcasts sound:

- Set your brand's tone and style in Hi, Moose
- Podcasts will match your brand voice automatically
- See [Brand Voice Settings](../brand-voice.md) for configuration

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
- Check Hi, Moose settings and documentation
- Verify subscription and credits

### Useful Links

- **Plugin page**: [wordpress.org/plugins/listen-to-this-article](https://wordpress.org/plugins/listen-to-this-article/)
- **Hi, Moose dashboard**: [himoose.com/dashboard](https://himoose.com/dashboard)
- **Podcast Generator docs**: [Podcast Generator](../features/podcast-generator.md)
- **Support**: support@himoose.com

---

## FAQ

**Q: Does this work with Gutenberg?**  
A: Yes! The plugin works with Gutenberg, Classic Editor, and most page builders.

**Q: Are audio files hosted on my server?**  
A: No, audio is hosted by Hi, Moose. This saves your server storage and bandwidth.

**Q: Can I download the audio files?**  
A: Yes, both you and your visitors can download the MP3 files if enabled.

**Q: Does this affect my site speed?**  
A: No, audio is loaded on-demand. The player is lightweight and doesn't slow page loads.

**Q: Can I use custom voices?**  
A: Yes! Generate custom podcasts in Hi, Moose with your preferred voices, then embed using shortcode.

**Q: How much does it cost?**  
A: The WordPress plugin is **free**. Podcast generation uses your Hi, Moose plan credits.

**Q: Can I generate podcasts for old posts?**  
A: Absolutely! Use bulk generation to add audio to existing content.

**Q: Does it work with WooCommerce?**  
A: Yes, you can generate podcasts for product descriptions if enabled in settings.

---

**Ready to make your content more accessible?** Install the plugin from [WordPress.org](https://wordpress.org/plugins/listen-to-this-article/) and start generating podcasts today!
