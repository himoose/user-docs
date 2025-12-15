# How to Create Versus Pages in Hi, Moose

## What This Helps You Do

The Versus Content Wizard lets you create dozens (or hundreds) of **comparison pages** at scale—like "Product A vs Product B"—without writing each page from scratch.

You define your comparison criteria once (pricing, features, integrations, etc.), add your competitors, and Hi, Moose generates AI-powered comparison content, hero images, and structured data for every possible pairing. Then you can export everything to CSV or push it directly to Webflow CMS.

This is programmatic SEO for comparison pages: capture high-intent search traffic (people researching "X vs Y") with unique, data-driven content that's optimized for both Google and AI Overviews.

---

## When to Use This

- **SaaS comparison marketing**: Create "YourProduct vs Competitor" pages for every major competitor (e.g., "Slack vs Microsoft Teams," "HubSpot vs Salesforce").
- **Ecommerce product comparisons**: Generate pages for "Product A vs Product B" across your catalog (useful for furniture, electronics, fashion).
- **Service provider directories**: Compare agencies, consultants, or local services (e.g., "Agency A vs Agency B").
- **Capture bottom-of-funnel traffic**: People searching "X vs Y" are close to buying—these pages convert.
- **Competitive intelligence**: Document how your brand stacks up against competitors across dozens of attributes.

Use this when you have **2+ competitors** and want to create **comparison content at scale**. If you only need one comparison page, you can still use this—but the real power is in generating 10, 50, or 100+ pages automatically.

---

## Before You Start

### What You Need

1. **A list of competitors**: At least 2 competitors (brands, products, or services you want to compare). You can add as many as you want—the wizard generates comparisons for every possible pairing.

2. **Comparison criteria**: Decide what attributes to compare (e.g., pricing, features, integrations, support, free trial, mobile app). These become your "schema."

3. **Your brand's data** (optional but recommended): If you want to include your own brand in the comparisons (not just competitor-to-competitor), you'll add your brand info in Step 3.

4. **Background image** (optional): A custom background for the auto-generated hero images. If you skip this, Hi, Moose uses a default.

5. **Subscription tier**:
   - **Free**: Schema and data entry only—no AI content generation.
   - **Starter, Growth, Enterprise**: Full AI content generation (intros, conclusions, hero images).

6. **Webflow API key** (optional): Only needed if you want to export directly to Webflow CMS. Otherwise, export to CSV.

### Important Notes

- The wizard has **8 steps**. You can jump between steps if you've already completed them (the wizard remembers your progress).
- Content generation uses AI credits. Check your plan's limits before generating content for 100+ comparisons.
- If you use **BYOK (Bring Your Own Key)**, you'll see estimated token costs before generating content.

---

## Step-by-Step (in Hi, Moose)

### Step 1: Define Schema

**What this step does**: You define the comparison attributes (called "categories" and "features") that will be used for all competitors.

#### How to Define Your Schema

1. In the wizard, you'll see: **"Do you want to include a comparison matrix?"**
   - Click **Yes** if you want structured comparisons (recommended).
   - Click **No** if you only want basic competitor cards (skips the matrix).

2. If you click **Yes**, you'll see the schema builder:

   **Add Categories**:
   - A category is a group of features (e.g., "Pricing," "Features," "Support").
   - Type a category name (e.g., "Pricing") and click **Add Category**.

   **Add Features to Each Category**:
   - Select a category from the dropdown.
   - Type a feature name (e.g., "Starting Price," "Free Trial").
   - Choose a feature type:
     - **Boolean** (Yes/No): For features that are either available or not (e.g., "Mobile App").
     - **Text**: For open-ended values (e.g., "Starting Price: $29/month").
     - **Numeric**: For numbers (e.g., "Max Users: 50").
   - Click **Add Feature**.

3. Repeat until you've added all your comparison criteria.

**Example schema**:
- **Pricing**
  - Starting Price (Text)
  - Free Trial (Boolean)
  - Money-Back Guarantee (Boolean)
- **Features**
  - Mobile App (Boolean)
  - Integrations (Numeric)
  - API Access (Boolean)
- **Support**
  - 24/7 Support (Boolean)
  - Live Chat (Boolean)

4. Click **Save & Continue** to move to Step 2.

**Can I edit the schema later?**  
Yes. The wizard loads your saved schema if you return to Step 1. You can add/remove categories or features anytime. **Warning**: Deleting a feature removes it from all competitors you've already added.

---

### Step 2: Add Competitors

**What this step does**: You add each competitor (brand, product, or service) and fill in their data for each feature.

#### How to Add a Competitor

1. Click **Add Competitor**.
2. Fill in the basic info:
   - **Name**: The competitor's name (e.g., "Slack").
   - **Slug**: A URL-friendly version of the name (e.g., "slack"). This is used in comparison page URLs.
   - **Short Description**: A 1-2 sentence summary (e.g., "Slack is a team messaging platform").
   - **Long Description**: A longer overview (optional). You can generate this with AI by clicking the **sparkle icon** (✨).

3. Upload logos:
   - **Full Logo URL**: Upload the competitor's full horizontal logo (e.g., logo with text).
   - **Logo Mark URL**: Upload just the logo icon/mark (e.g., the Slack hashtag symbol).
   - If you don't upload a logo, Hi, Moose generates a text-based logo placeholder.

4. Fill in the matrix data:
   - You'll see tabs for each category you defined in Step 1 (e.g., "Pricing," "Features").
   - For each feature, enter the value:
     - **Boolean**: Toggle on/off (Yes/No).
     - **Text**: Type the value (e.g., "$29/month").
     - **Numeric**: Enter a number (e.g., "50").

5. Click **Save Competitor**.

**Repeat for all competitors**. You need at least 2 competitors to generate comparisons.

**Tips**:
- Use the **AI Generate** button next to "Short Description" or "Long Description" to auto-generate copy based on the competitor name and website.
- If you're adding many competitors, consider exporting a CSV template (you can import it later—this feature may vary by platform).

---

### Step 3: Your Brand

**What this step does**: Add your own brand's data so it can be included in comparisons (e.g., "YourBrand vs Slack").

This is optional—if you skip it, the wizard generates **competitor-to-competitor** comparisons only (e.g., "Slack vs Microsoft Teams").

#### How to Add Your Brand

1. Fill in your brand info:
   - **Name**: Your brand or product name.
   - **Website**: Your website URL.
   - **Short Description**: A 1-2 sentence pitch.

2. Fill in the matrix data (same as Step 2):
   - You'll see the same categories and features.
   - Enter your brand's values for each feature.

3. Click **Save & Continue**.

**Why include your brand?**  
If you include it, Hi, Moose generates **three-way comparisons** where your brand is always positioned as the best choice. For example:
- Intro: "Comparing Slack, Microsoft Teams, and YourBrand."
- Conclusion: "While Slack and Teams are solid, YourBrand offers [unique advantages]."

If you skip this step, comparisons are neutral (just competitor A vs competitor B).

---

### Step 4: Generate Comparisons

**What this step does**: Hi, Moose creates a **comparison record** for every possible pairing of competitors.

For example:
- 3 competitors = 3 comparisons (A vs B, A vs C, B vs C)
- 5 competitors = 10 comparisons
- 10 competitors = 45 comparisons

#### How to Generate Comparisons

1. You'll see a summary:
   - **Total Comparisons**: How many pairings will be created.
   - **Missing Comparisons**: If you've previously generated some, this shows what's left.

2. Click **Generate Comparisons**.

3. Hi, Moose creates the pairing records in your database. This is fast (1–2 seconds per comparison).

4. Once done, click **Next**.

**What gets created?**  
Each comparison is a **slug** (e.g., "slack-vs-microsoft-teams") with metadata pointing to the two competitors. No content yet—that happens in Step 5.

**If you add more competitors later**: Return to Step 4 and click **Generate Comparisons** again. Hi, Moose only creates new pairings (doesn't duplicate existing ones).

---

### Step 5: Generate Content

**What this step does**: Hi, Moose writes AI-generated **intro** and **conclusion** paragraphs for each comparison page.

#### How to Generate Content

1. You'll see two tabs:
   - **Introduction**: AI writes an opening paragraph explaining what's being compared.
   - **Conclusion**: AI writes a closing paragraph summarizing the best choice (or highlighting key differences).

2. Click **Generate All Introductions** or **Generate All Conclusions**.

3. Hi, Moose generates content for all comparisons in batches:
   - You'll see a progress bar (e.g., "5/45 comparisons generated").
   - For BYOK users, you'll see estimated token usage and cost before confirming.

4. Once done, you can:
   - **Preview** any comparison to see the generated intro/conclusion.
   - **Edit** the content using the rich text editor.
   - **Regenerate** individual comparisons if you don't like the output.

5. Click **Save & Continue** when satisfied.

**What does the AI write?**  
- **Introduction**: Explains what's being compared, who it's for, and what the reader will learn. Example: *"Slack and Microsoft Teams are both popular collaboration tools. This comparison helps teams decide which one fits their needs."*
- **Conclusion**: Summarizes the winner (if your brand is included) or the best fit for different use cases. Example: *"Slack is best for startups prioritizing ease of use, while Teams excels for enterprises already using Microsoft 365."*

**If your brand is included**: The conclusion will subtly position your brand as the best option, with Slack and Teams as alternatives.

**Tips**:
- Generate all content at once, then edit a few manually if needed.
- Use the **Edit** button to refine AI output—it's faster than writing from scratch.

---

### Step 6: Generate Images

**What this step does**: Hi, Moose creates **hero images** for each comparison page—side-by-side competitor logos on a background.

#### How to Generate Images

1. **Upload a background image** (optional):
   - Click **Upload Background Image**.
   - Choose a branded image (e.g., your website's gradient, abstract pattern).
   - If you skip this, Hi, Moose uses a default gradient.

2. **Choose logo style**:
   - **Full Logo**: Uses the full horizontal logo.
   - **Logo Mark**: Uses just the logo icon (recommended if your competitors have strong icon marks).

3. Click **Generate All Images**.

4. Hi, Moose creates a hero image for each comparison:
   - Competitor A logo on the left.
   - "vs" in the center.
   - Competitor B logo on the right.
   - Your background image behind everything.

5. Preview the images in the list. You can regenerate if needed.

6. Click **Save & Continue**.

**What if competitors don't have logos?**  
Hi, Moose generates text-based placeholders (e.g., a colored square with the first letter).

**Can I skip this step?**  
Yes. Images are optional—you can export without them and add images manually later in Webflow or your CMS.

---

### Step 7: Export

**What this step does**: Export your comparison data as CSV files or push directly to Webflow CMS.

#### Option 1: Export to CSV

1. Click **Export CSV**.
2. Hi, Moose downloads two files:
   - **competitors.csv**: All competitor data (name, slug, features).
   - **comparisons.csv**: All comparison data (slug, competitor A, competitor B, intro, conclusion, image URL).

3. Use these CSVs to import into your CMS, database, or custom website.

#### Option 2: Send to Webflow

**Requirements**:
- Your project must have a **Webflow API Key** and **Site ID** configured.
- Go to **Projects** → **Edit Project** → Webflow Configuration to set this up.

**How to Send to Webflow**:

1. Click **Send to Webflow**.
2. Hi, Moose checks for existing collections:
   - If this is your **first time**, it creates two new CMS collections:
     - **Competitors pSEO**: Stores all competitor data.
     - **Comparisons pSEO**: Stores all comparison pages.
   - If collections **already exist**, you'll see a modal asking:
     - **Replace All**: Delete old data and upload fresh data.
     - **Update Only**: Update existing items, add new ones (preserves manual edits).

3. Confirm your choice. Hi, Moose uploads:
   - All competitors to the **Competitors pSEO** collection.
   - All comparisons to the **Comparisons pSEO** collection.
   - Images, intros, conclusions, and matrix data.

4. Once done, you'll see a success message.

**Choose whether to publish**:
- **Staged**: Items are created as drafts in Webflow (not live yet).
- **Publish After Upload**: Hi, Moose publishes the collections after upload (items go live immediately).

**What gets created in Webflow?**  
- **Competitors pSEO** collection with fields: name, slug, short-description, long-description, logo-url, logo-mark-url, and all your custom matrix fields (e.g., pricing-starting-price, features-mobile-app).
- **Comparisons pSEO** collection with fields: slug, competitor-a (reference), competitor-b (reference), introduction, conclusion, hero-image.
- You can build a collection template page in Webflow to display these comparison pages.

5. Click **Next** to finish.

---

### Step 8: Webflow Setup

**What this step does**: Instructions for creating comparison page templates in Webflow Designer.

This step shows you:
- How to create a **Collection Template Page** in Webflow for the "Comparisons pSEO" collection.
- How to bind dynamic fields (competitor names, logos, intro, conclusion, matrix data) to your template.
- Best practices for URL slugs and SEO settings.

**This is documentation only—no actions in Hi, Moose.** Click **Finish** to complete the wizard.

---

## What You Get (Outputs)

After completing the wizard, you have:

- **Competitor database**: Every competitor with structured matrix data (pricing, features, support, etc.).
- **Comparison pages**: Every possible pairing (e.g., 10 competitors = 45 comparisons).
- **AI-generated content**: Intros and conclusions for each comparison.
- **Hero images**: Side-by-side logo images for each comparison.
- **CSV exports**: Downloadable data files for import into any CMS.
- **Webflow CMS collections** (optional): Fully structured collections ready to display as comparison pages.

You can now build a **programmatic SEO site** targeting long-tail "X vs Y" keywords at scale.

---

## Tips for Best Results

1. **Start small, then scale**: Add 3–5 competitors first to test the workflow. Once you're happy with the schema and content quality, add the rest.

2. **Use specific feature names**: Instead of "Feature 1," use "Mobile App" or "API Access." This makes AI-generated content more accurate.

3. **Include your brand for positioning**: If you add your brand in Step 3, the conclusions will subtly favor your product—great for bottom-of-funnel content.

4. **Generate content in batches**: If you have 100+ comparisons, generate content for 10–20 at a time. This avoids rate limits and lets you review output quality before committing.

5. **Edit AI output**: The AI is good, but not perfect. Edit intros/conclusions to add your unique insights, customer quotes, or brand voice.

6. **Use high-quality logos**: Uploaded logos look more professional than auto-generated text logos. Aim for transparent PNGs (500x200px for full logos, 250x250px for marks).

7. **Choose a branded background**: Custom backgrounds make your hero images stand out. Use your brand's gradient, texture, or pattern.

8. **Publish staged first**: When sending to Webflow, choose "Staged" so you can review pages in Webflow Designer before publishing live.

9. **Update regularly**: If competitors change pricing or features, update their data in Step 2, then regenerate comparisons/content. The wizard preserves your edits where possible.

10. **Track performance**: After publishing, monitor which comparison pages get traffic. Double down on high-performers by adding more detail or related content.

---

## Troubleshooting

### 1. "No matrix structure found. Please complete the previous steps first."

**Why**: You tried to skip to Step 2 without completing Step 1 (Define Schema).

**Fix**:
- Go back to **Step 1: Define Schema**.
- Add at least one category and one feature.
- Click **Save & Continue**.
- Now you can proceed to Step 2.

---

### 2. Can't generate comparisons—"You need at least 2 competitors"

**Why**: You only added 0 or 1 competitors in Step 2.

**Fix**:
- Go back to **Step 2: Add Competitors**.
- Add at least 2 competitors (each with a name and slug).
- Save them.
- Return to Step 4 and click **Generate Comparisons**.

---

### 3. AI content generation fails or is slow

**Why**: Rate limits, API timeout, or insufficient credits.

**Fix**:
- **Check your credits**: Go to **Settings** → **Subscription** to see your remaining AI credits.
- **Wait and retry**: If you hit a rate limit, wait 60 seconds and try again.
- **Generate in smaller batches**: Instead of generating all 100 comparisons at once, do 10–20 at a time.
- **BYOK users**: Make sure your OpenAI API key is valid and has sufficient funds.

---

### 4. Images fail to generate—"Failed to load image" error

**Why**: Uploaded logo URLs are not accessible, or CORS issues prevent loading.

**Fix**:
- Make sure uploaded logos are **public** (not behind authentication).
- Use **transparent PNG files** for logos (not JPG).
- If using external URLs, host them on a CORS-friendly CDN (like Cloudinary or Firebase Storage).
- Re-upload logos directly in Hi, Moose instead of using external URLs.

---

### 5. "Webflow API key is required" error

**Why**: You clicked **Send to Webflow** but haven't configured a Webflow API key.

**Fix**:
1. Go to [Webflow Dashboard](https://webflow.com/dashboard/workspace/sites) → Workspace Settings → Integrations → API Access.
2. Create a new API token with these permissions:
   - **Sites** → Read and Write
   - **CMS** → Read and Write
   - **Assets** → Read and Write
3. Copy the token.
4. In Hi, Moose, go to **Projects** → **Edit Project** → Webflow Configuration.
5. Paste your API key and Site ID.
6. Save.
7. Return to Step 7 and try **Send to Webflow** again.

---

### 6. Webflow upload succeeds but pages don't appear

**Why**: Items were created as **staged (draft)**, not published.

**Fix**:
- In Webflow Designer, go to the **CMS** tab.
- Select the **Comparisons pSEO** collection.
- Select all items and click **Publish**.
- Alternatively, return to Hi, Moose Step 7 and choose **Publish After Upload** next time.

---

### 7. Comparisons show "undefined" or missing data

**Why**: Competitors are missing required fields (name, slug, or matrix data).

**Fix**:
- Go back to **Step 2: Add Competitors**.
- Open each competitor and make sure **Name** and **Slug** are filled in.
- Fill in all required matrix fields (marked with *).
- Save each competitor.
- Return to Step 4 and click **Regenerate Comparisons** (if needed).

---

### 8. Schema changes don't update existing competitors

**Why**: Existing competitors were created with the old schema. Adding a new feature doesn't retroactively fill data.

**Fix**:
- Go to **Step 2: Add Competitors**.
- Open each competitor and scroll to the new feature.
- Fill in the value manually.
- Save.

**Note**: Deleting a feature from the schema **does** cascade-delete it from all competitors.

---

### 9. "Existing collections found. Please confirm how to proceed."

**Why**: You've already sent data to Webflow, and Hi, Moose is asking whether to replace or update.

**Fix**:
- **Replace All**: Choose this if you want to delete old data and start fresh. **Warning**: This deletes all manual edits you made in Webflow.
- **Update Only**: Choose this if you want to preserve existing items and only update/add new ones. Safer for incremental updates.

Make your choice in the modal, then confirm.

---

### 10. Slow performance when navigating wizard steps

**Why**: The wizard loads all project data (competitors, comparisons) on mount to allow free navigation.

**Fix**:
- Wait for the "Loading project data..." spinner to finish before clicking step indicators.
- If you have 100+ competitors and 1,000+ comparisons, initial load may take 5–10 seconds. Subsequent navigation is instant.
- Clear your browser cache if the issue persists.

---

## Frequently Asked Questions

### How many comparisons will be generated?

The number of comparisons is calculated as:  
**n × (n - 1) / 2**

Where **n** = number of competitors.

Examples:
- 2 competitors = 1 comparison
- 3 competitors = 3 comparisons
- 5 competitors = 10 comparisons
- 10 competitors = 45 comparisons
- 20 competitors = 190 comparisons

If you include your brand in Step 3, it's counted as one of the competitors.

---

### Can I edit comparisons after generating content?

Yes. Go to **Step 5: Generate Content**, select a comparison, and click **Edit**. You can modify the intro or conclusion using the rich text editor.

Changes are saved to your database immediately.

---

### What happens if I delete a competitor?

If you delete a competitor:
- All comparisons involving that competitor are also deleted (cascade delete).
- Generated content, images, and CSV exports will no longer include that competitor.

To delete a competitor, go to **Step 2: Add Competitors**, find the competitor, and click **Delete** (trash icon).

---

### Can I regenerate content for just one comparison?

Yes. In **Step 5: Generate Content**, click on a specific comparison, then click **Regenerate Introduction** or **Regenerate Conclusion**. This overwrites the existing content for that comparison only.

---

### What if my competitors don't have logos?

Hi, Moose generates **text-based logo placeholders**:
- **Full logo**: The competitor's name in bold text.
- **Logo mark**: The first letter of the competitor's name on a colored background.

You can upload real logos later by editing the competitor in Step 2.

---

### Can I use this for non-SaaS industries?

Yes. The Versus Content Wizard works for any industry:
- **Ecommerce**: Compare products (phones, laptops, furniture).
- **Services**: Compare agencies, consultants, or local businesses.
- **Education**: Compare courses, bootcamps, or universities.
- **Healthcare**: Compare insurance plans, clinics, or treatments.

Just adjust your schema (Step 1) to fit your industry (e.g., "Price," "Location," "Certification").

---

### Does the AI favor my brand in comparisons?

**If you include your brand in Step 3**: Yes. The AI generates conclusions that subtly position your brand as the best choice while acknowledging competitor strengths. This is intentional—it's for **your** marketing site.

**If you skip Step 3**: No. Comparisons are neutral and focus on helping the reader choose between competitors based on their needs.

---

### How do I publish comparison pages in Webflow?

After sending data to Webflow (Step 7), you need to:

1. Go to Webflow Designer.
2. Open the **CMS** tab.
3. Select the **Comparisons pSEO** collection.
4. Create a **Collection Template Page** (or use an existing one).
5. Bind dynamic fields:
   - **Hero Image**: Bind to the `hero-image` field.
   - **Competitor A Name**: Bind to `competitor-a → name`.
   - **Competitor A Logo**: Bind to `competitor-a → logo-url`.
   - **Introduction**: Bind to `introduction` (rich text).
   - **Conclusion**: Bind to `conclusion` (rich text).
   - **Matrix data**: Bind each matrix field (e.g., `pricing-starting-price`) to text elements.
6. Publish the template page.

Your comparisons will now be live at URLs like `yoursite.com/comparisons/slack-vs-microsoft-teams`.

---

### Can I add more competitors later?

Yes. Just return to **Step 2: Add Competitors** and add new ones. Then:
- Go to **Step 4** and click **Generate Comparisons** to create new pairings.
- Go to **Step 5** to generate content for the new comparisons.
- Go to **Step 6** to generate images.
- Go to **Step 7** to export or send to Webflow again.

The wizard only creates **new** comparisons—it doesn't duplicate existing ones.

---

### What's the difference between "Replace All" and "Update Only"?

When sending to Webflow for the **second time**, you'll see these options:

- **Replace All**: Deletes all existing items in the Webflow CMS collections and uploads fresh data from Hi, Moose. **Warning**: Any manual edits you made in Webflow will be lost.
- **Update Only**: Updates existing items (by slug) and adds new items, but preserves items not present in Hi, Moose. Safer for incremental updates.

**Recommendation**: Use **Update Only** unless you've completely restructured your schema and want to start fresh.

---

### Can I use this without Webflow?

Yes. You can export to **CSV** (Step 7) and import into:
- WordPress (with a CSV import plugin)
- Custom website or app (via database import)
- Google Sheets (for review or collaboration)
- Other CMS platforms (Contentful, Strapi, etc.)

Webflow is optional—it's just the fastest way to go from Hi, Moose to a live site.

---

### How much does AI content generation cost?

**For standard plans** (Starter, Growth, Enterprise):
- AI credits are included in your subscription.
- Check **Settings** → **Subscription** to see your limits.

**For BYOK (Bring Your Own Key) users**:
- You pay OpenAI directly (billed to your OpenAI account).
- Before generating content, Hi, Moose shows estimated token usage and cost.
- Example: 50 comparisons ≈ 25,000 tokens ≈ $0.25 (varies by model).

---

### Can I customize the AI-generated content?

Yes. The AI is a starting point—you should **edit** the content to:
- Add your unique insights or customer quotes.
- Adjust tone to match your brand voice.
- Include specific data points or testimonials.
- Fix any inaccuracies (AI sometimes hallucinates).

Use the **Edit** button in Step 5 to modify intros/conclusions with the rich text editor.

---

### What if I want to compare more than 2 products per page?

The wizard creates **pairwise comparisons** (A vs B). For three-way comparisons (A vs B vs C), you'd need to:
- Manually create a custom page in Webflow or your CMS.
- Pull data from multiple comparison records.

Programmatic three-way comparisons aren't supported yet, but you can request this feature via [Support](https://www.himoose.com/contact).

---

### Why are some comparisons marked "_needsRefresh"?

In **Step 4**, you may see comparisons flagged with `_needsRefresh: true`. This means:
- One of the competitors was updated after the comparison was last generated.
- You should regenerate content (Step 5) and images (Step 6) to reflect the latest data.

Hi, Moose tracks timestamps to auto-detect stale comparisons.

---

### Can team members use the Versus Content Wizard?

Yes. Team members (Admins and Members) can use the wizard. They inherit the project owner's subscription tier for AI features.

**Permissions**:
- **Admins**: Can edit all wizard steps, generate content, and export.
- **Members**: Can view and edit (depending on project permissions).
- **Viewers**: Read-only access (can't edit or generate).

---

### How do I optimize comparison pages for SEO?

**In Hi, Moose**:
- Use descriptive slugs (e.g., "slack-vs-microsoft-teams," not "comp-1").
- Write unique intros/conclusions—don't rely on AI alone.
- Include your brand (Step 3) to differentiate from generic comparison sites.

**In Webflow (or your CMS)**:
- Set SEO titles: *"Slack vs Microsoft Teams: Which is Best for Your Team?"*
- Write meta descriptions that include both competitor names and a CTA.
- Add structured data (JSON-LD) for comparison pages—helps with rich snippets.
- Interlink related comparisons (e.g., "See also: Slack vs Asana").

**Content tips**:
- Expand matrix data into prose (don't just show a table).
- Add screenshots or video demos.
- Link to official competitor pages and reviews (builds trust).

---

## Related Features

- **Content Brief Creator**: Generate data-driven content briefs for your comparison pages. See [SEO Content Briefs](content-briefs.md).
- **AEO Tools**: Analyze how AI engines interpret your comparison pages. See [AEO Optimization](aeo-optimization.md).
- **Webflow Content Manager**: Manage your Webflow CMS collections (including Comparisons pSEO) directly in Hi, Moose. See [Webflow Integration](../integrations/webflow.md).

---

**Still stuck?** Check the [Support](https://www.himoose.com/contact) page or email support@himoose.com. Include your project ID and which wizard step you're on for faster help.
