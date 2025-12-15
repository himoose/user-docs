# How to Generate FAQs in Hi, Moose

## What this helps you do

Create FAQ sections that answer real questions your audience asks. Hi, Moose generates natural, conversational questions (not robotic chatbot output) and provides concise answers based on your content.

**Why Hi, Moose FAQs are better than generic AI:**
- **Gap-filling intelligence** — Identifies questions readers would ask that aren't explicitly answered yet
- **Brand voice integration** — FAQs match your tone and style automatically
- **SEO-ready schema markup** — Includes structured data for Google rich results
- **Question quality** — Natural language questions real humans would ask, not keyword-stuffed queries

FAQs improve user experience, reduce support requests, and boost SEO by answering user intent directly on the page.

## When to use this

- **Product pages** — Answer common pre-purchase questions
- **Service pages** — Clarify what you offer and how it works
- **Blog posts** — Provide quick answers to reader questions
- **Documentation** — Supplement technical content with accessible FAQs
- **Landing pages** — Address objections and build trust
- **Support content** — Reduce repetitive customer service inquiries

Best for pages with substantial content (300+ words). FAQs work on any page where visitors have questions.

## Before you start (requirements)

### Required
- A project selected in Hi, Moose
- Either:
  - A published webpage URL (publicly accessible), OR
  - Content ready to paste manually

### Optional
- Brand Voice settings configured (FAQs will match your tone)
- Webflow API key (if you want automatic updates to Webflow CMS)

### Note on API keys
- **Free & Standard plans**: Use Hi, Moose's API keys automatically
- **BYOK plans**: Your OpenAI API key must be saved in Settings

## Step-by-step (in Hi, Moose)

### Method 1: From URL

#### 1. Select input mode
- Click the **From URL** tab (selected by default)
- Globe icon indicates URL input mode

#### 2. Enter webpage URL
- Paste your page's full URL in the text field
- Example: `https://yourwebsite.com/product-page`
- The URL must be publicly accessible

#### 3. Generate FAQs
- Click **Generate FAQs** (or **Generate Questions** in Marketer Mode)
- Hi, Moose will:
  - Extract content from the page
  - Analyze gaps and user intent
  - Generate natural FAQ questions and answers
  - Create schema markup automatically

**Status indicators**:
- "Extracting..." — Fetching page content
- "Generating..." — AI is creating FAQs
- Success — Green preview box appears with results

#### 4. Review extracted content
- You'll see your content in a gray box
- Character count displays (e.g., "Content (3,456 chars)")
- Verify content is complete

#### 5. Edit FAQs (optional)
- Use the rich text editor to modify questions or answers
- Add, remove, or reorganize FAQ pairs
- Adjust wording to match your brand
- Format text: **bold**, *italic*

#### 6. Save changes
- If you edited: Click **Save Changes** button
- Saves edits for future reference
- Button shows "Saving..." while processing

#### 7. Copy to your website
**Two options:**

**Option A - Copy HTML:**
- Click **Copy HTML** button (purple)
- Pastes FAQ section with proper `<div id="faq-section">` wrapper
- Paste into your CMS where you want FAQs to appear

**Option B - Copy Schema:**
- Click **Copy Schema** button to copy structured data
- Paste schema markup in your page's `<head>` section
- Enables Google FAQ rich results in search

**Pro tip**: Use both — HTML for visible FAQs and schema for SEO.

### Method 2: Paste Content

#### 1. Select input mode
- Click the **Paste Content** tab
- Document icon indicates manual input

#### 2. Paste your content
- Copy content from your page/document
- Paste into the large text area
- Plain text only (no formatting preserved)

#### 3. Generate FAQs
- Click **Generate FAQs** (green button)
- AI processes your content
- Results appear in editable preview

#### 4. Follow steps 5-7 from Method 1
- Edit, save, and copy as described above

### Additional features

#### Export CSV
- Click **Export CSV** button (yellow)
- Downloads CSV with URL, questions, and answers
- Useful for documentation or batch records

#### Update in Webflow (if configured)
- **Update in Webflow** button appears if:
  - Project platform is set to Webflow
  - Webflow API key exists in settings
- Select collection and update CMS items directly
- Only available after saving changes

#### View Schema Preview
- Click **View Schema** toggle to see structured data
- Shows JSON-LD format for FAQPage markup
- Validation indicator shows if schema is correct
- Green = valid, Red = needs fixing

## What you get (outputs)

### FAQ section
- 4-8 natural question/answer pairs
- Questions written as real users would ask them
- Answers: 1-3 concise sentences (no fluff)
- Formatted as clean HTML with proper markup

### HTML structure
```html
<div id="faq-section">
  <ul>
    <li>
      <p><strong>What is X?</strong></p>
      <p>Brief answer explaining X clearly.</p>
    </li>
    <li>
      <p><strong>How does Y work?</strong></p>
      <p>Brief answer about Y.</p>
    </li>
  </ul>
</div>
```

### Schema markup (FAQPage)
- Structured data in JSON-LD format
- Follows Google's FAQPage guidelines
- Enables rich results in search
- Includes all questions and answers
- Pre-validated and ready to use

### Example schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is X?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Brief answer explaining X."
      }
    }
  ]
}
```

### Editable format
- Rich text editor with formatting controls
- Bold, italic, lists
- Live preview of changes
- Saved to project history

## Tips for best results

### Content preparation
- **Use complete pages** — More content = better question identification
- **Clean URLs work best** — Avoid preview links or password-protected pages
- **Well-structured content** — Pages with clear sections produce better FAQs
- **Optimal length**: 500-3000 words yields 5-7 strong FAQs

### When to use manual paste
- URL extraction fails (Cloudflare, JavaScript-heavy sites)
- Content is in a draft (Google Docs, Word)
- Page behind paywall or login
- You want FAQs for content not yet published
- Testing FAQ quality before page goes live

### Editing best practices
- **Keep answers concise** — 1-3 sentences max
- **Natural questions** — Write like your customers talk
- **Add specifics** — Include product names, pricing, features
- **Front-load value** — Most important FAQs first
- **No marketing hype** — Direct, helpful answers only
- **Link to details** — Reference other pages for deep dives

### Schema implementation
**Where to place schema:**
- WordPress: Use schema plugin or paste in `<head>` via theme
- Webflow: Add in Page Settings → Custom Code → Head
- Shopify: Add to theme.liquid file in `<head>` section
- Custom sites: Paste before closing `</head>` tag

**Schema best practices:**
- Only one FAQPage schema per page
- Don't include schema for fake/marketing FAQs
- Questions should actually appear on the page
- Answers must match visible content
- Test with Google's Rich Results Test tool

### CMS implementation
- **WordPress**: Paste HTML in "Text" editor mode (not Visual)
- **Webflow**: Use Rich Text element for HTML, Embed for schema
- **Shopify**: Use HTML content blocks
- **Custom sites**: Target `#faq-section` for custom styling

### Brand voice integration
- Configure Brand Voice in Settings for better FAQs
- Upload brand documents or set tone guidelines
- FAQs automatically match your style
- Works across all plan tiers (except Free tier)

### Question quality
Hi, Moose generates questions that:
- **Fill gaps** — Address topics not explicitly covered
- **Anticipate intent** — What readers would naturally ask
- **Avoid duplication** — Don't restate existing headings
- **Sound human** — Natural language, not robotic

## Troubleshooting

### ❌ "Extraction too short" or "Content too short"
**Problem**: URL extraction returned insufficient content (less than 120 characters).

**Fix**:
- Check URL is correct and publicly accessible
- Try in incognito browser to test access
- Remove URL parameters (`?preview=true`, etc.)
- Switch to **Paste Content** tab and paste manually
- If page loads content via JavaScript, manual paste required
- Check for bot protection (Cloudflare, captchas)

---

### ❌ Only 2-3 FAQs generated instead of 4-8
**Problem**: Content too short or doesn't contain enough question-worthy topics.

**Fix**:
- Ensure source content is at least 500 words
- Check extracted content (gray box) is complete
- Page may have mostly images/videos (little text)
- Try pasting full article content manually
- Combine multiple pages into one paste for more FAQs
- Consider if content actually needs FAQs (very short pages may not)

---

### ❌ FAQs don't match my brand voice
**Problem**: Generated FAQs sound generic or off-brand.

**Fix**:
- Set up Brand Voice in Project Settings
- Upload sample documents showing your tone
- Specify tone guidelines (formal, casual, technical, etc.)
- Edit FAQs manually after generation
- **Note**: Free plans don't include brand voice integration
- Regenerate after configuring brand voice

---

### ❌ Schema validation errors or red indicator
**Problem**: Schema markup has formatting issues or missing fields.

**Fix**:
- Click **View Schema** to see specific errors
- Most common: Empty answer text (edit FAQ to add content)
- Check for special characters in questions/answers (may break JSON)
- Copy schema and test in Google's Rich Results Test
- If errors persist, regenerate FAQs from scratch
- Ensure at least one complete Q&A pair exists

---

### ❌ "Save Changes" button grayed out or not working
**Problem**: Can't save FAQ edits.

**Fix**:
- Make sure you actually changed something (button only appears if edited)
- Check internet connection
- Look for error toast notifications (red)
- Try copying content and regenerating
- Browser console may show errors (F12 → Console)
- Clear browser cache and refresh

---

### ❌ FAQs lost formatting when pasted in CMS
**Problem**: HTML formatting doesn't appear in WordPress/Webflow.

**Fix**:
- Use **Copy HTML** button (don't manually select and copy)
- WordPress: Switch to "Text" or "Code Editor" (not Visual)
- Webflow: Use Rich Text element, not plain text
- Don't paste into visual/WYSIWYG editors
- Paste in HTML/code mode only
- Some CMS platforms strip custom HTML (check settings)

---

### ❌ Google not showing FAQ rich results
**Problem**: Schema markup doesn't produce rich results in search.

**Fix**:
- Test schema with Google's Rich Results Test tool
- Ensure schema is in page `<head>` or `<body>` (not external file)
- FAQs must actually appear on the page (visible to users)
- Google may not show rich results for every query
- Page must be indexed (check Google Search Console)
- Can take 2-4 weeks for Google to process new schema
- Verify schema follows Google's guidelines exactly

---

### ❌ "Team ID mismatch" or permission error
**Problem**: Authentication or team access issue.

**Fix**:
- Refresh page and log in again
- Verify you have access to the selected project
- Check subscription is active in Settings
- If using BYOK plan, ensure API key is saved
- Contact account owner if you're a team member
- Try logging out completely and back in

---

### ❌ Webflow button disabled or not visible
**Problem**: Can't update Webflow CMS with FAQs.

**Fix**:
- **If button disabled**: Save changes first, then try Webflow
- **If button missing**: 
  - Go to Project Settings
  - Set platform to "Webflow"
  - Add Webflow API key
  - Refresh page
- Verify API key has correct permissions
- Check Webflow site is accessible

---

### 🔄 Stuck on "Extracting..." or "Generating..."
**Problem**: Process takes longer than 60 seconds.

**Fix**:
- Wait up to 2 minutes for long content
- Check internet connection
- Refresh page and try again
- Test with different URL (may be site-specific issue)
- Use manual paste method instead
- Very long content (10,000+ words) may timeout

## FAQs

### How many FAQs will be generated?
Typically 4-8 FAQ pairs depending on content length and complexity. Longer, more detailed content produces more questions. Short pages (under 500 words) may only get 3-4 FAQs.

### Can I control what questions are generated?
Not directly, but you can:
- Edit questions after generation
- Regenerate for different results
- Use Brand Voice to influence tone
- Paste specific sections manually for focused FAQs

Always review and edit to ensure accuracy.

### How is this better than using ChatGPT directly?
Hi, Moose FAQs:
- **Identify content gaps** — Questions readers would ask that aren't explicitly answered
- **Natural language** — How real people talk, not keyword-stuffed
- **Brand voice aware** — Matches your tone automatically
- **Schema included** — Ready-to-use structured data
- **Question quality** — Avoids duplicating obvious headings
- **Smart analysis** — Understands user intent beyond surface keywords

Generic AI just summarizes what's there. Hi, Moose finds what's missing.

### Do FAQs update automatically if I change my page?
No. FAQs are generated once from a snapshot of your content. If you update your page significantly, regenerate FAQs by entering the URL again.

### What's the difference between "From URL" and "Paste Content"?
- **From URL**: Hi, Moose automatically extracts content from a live webpage
- **Paste Content**: You manually copy/paste content (useful for drafts, protected content, or when extraction fails)

Both methods produce identical FAQ quality.

### Can I use this for non-English content?
Yes, Hi, Moose supports 100+ languages. FAQs will be generated in the same language as your input content.

### Where should I place FAQs on my webpage?
**Best practices:**
- Near the bottom of main content (after detail sections)
- Above footer navigation
- In a dedicated "Frequently Asked Questions" section
- Don't place at the very top (readers haven't seen content yet)

**Product pages**: After product details, before reviews
**Blog posts**: After conclusion, before comments
**Service pages**: After benefits/features

### What HTML tags are included in the output?
Standard semantic HTML: `<div>`, `<ul>`, `<li>`, `<p>`, `<strong>`, `<em>`. Output is clean, accessible HTML safe for all CMS platforms.

### How do I style the FAQ section?
Use CSS to target `#faq-section`. Example:
```css
#faq-section {
  padding: 40px 20px;
  background: #f9f9f9;
}

#faq-section strong {
  color: #0066cc;
  font-size: 1.1em;
}
```

### Can I generate FAQs for multiple pages at once?
For single pages, use this feature. For bulk processing of many URLs, use the Batch Sitemap Processor (separate feature).

### Will this work with password-protected pages?
No. URL extraction only works with publicly accessible pages. For password-protected or draft content, use **Paste Content** method.

### What is FAQ schema markup and why does it matter?
Schema markup is structured data that helps Google understand your FAQs. Benefits:
- Enables FAQ rich results in search (blue expandable boxes)
- Increases click-through rates
- Improves visibility in search results
- Helps Google index your content better

Not all pages will show rich results (Google decides), but schema increases the likelihood.

### How do I test if my schema is working?
Use Google's Rich Results Test tool:
1. Copy your page URL
2. Go to: https://search.google.com/test/rich-results
3. Enter URL and test
4. Check for FAQPage validation
5. Fix any errors shown

### Can I edit FAQs after saving them?
Yes, saved FAQs are stored in your project history. Access History tab to view previous generations and edit again if needed.

### Does the "Manual" label affect the output?
No, the "Manual" label just indicates content source (pasted vs. URL). Manual and URL-extracted content are processed identically by the AI.

### How often should I regenerate FAQs?
- **Minimal content changes**: No need to regenerate
- **Major updates** (new features, pricing, etc.): Regenerate
- **Every 6-12 months**: Refresh to keep current
- **When adding new pages**: Generate for each new page

### What if I need more than 8 FAQs?
Break content into sections and generate separately, then combine:
- Products: Generate for different product features
- Services: Separate FAQs for pricing, process, support
- Long content: Paste specific sections for focused FAQs

Or manually add questions after generation using the editor.
