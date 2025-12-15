# How to Manage Your Settings in Hi, Moose

## What This Helps You Do

The Settings page lets you customize your Hi, Moose experience, manage your subscription, and configure AI services. 

You can update your account info (email, password), choose between **Marketer Mode** (simplified) or **SEO Mode** (advanced), connect your own OpenAI API key for unlimited AI usage, monitor your token consumption, and manage billing.

This is your control center for personalizing Hi, Moose to match your workflow, budget, and technical expertise.

---

## When to Use This

- **Switch experience modes**: Choose between Marketer Mode (for SMB teams) or SEO Mode (for SEO professionals) to adjust feature complexity.
- **Update account info**: Change your email, verify your email, or reset your password.
- **Bring Your Own Key (BYOK)**: Connect your OpenAI API key to bypass monthly token limits and use your own billing.
- **Select AI models**: Pick which GPT model to use (GPT-4.1, GPT-5, etc.) if you're on the BYOK plan.
- **Monitor usage**: Track your monthly AI token consumption to avoid hitting limits.
- **Manage subscription**: Update payment methods, change billing cycles, or cancel/reactivate your subscription.

---

## Before You Start

### What You Need

1. **Active Hi, Moose account**: You must be logged in to access Settings.

2. **For BYOK users**: 
   - An OpenAI API key from [platform.openai.com](https://platform.openai.com/api-keys).
   - Your own OpenAI billing account with sufficient funds.

3. **For team members**: You'll see your team owner's subscription plan. Most settings (like AI model selection) are personal, but subscription changes require owner access.

### Important Notes

- **Marketer Mode vs SEO Mode** affects the UI complexity—not your subscription features. Both modes have access to the same tools.
- **BYOK plans** require you to bring your own OpenAI API key. Without it, AI features won't work.
- **Team members** inherit the team owner's subscription tier but can set their own experience mode and AI model preferences (if BYOK).

---

## Step-by-Step (in Hi, Moose)

### 1. Access Settings

1. Click your profile icon (top-right corner).
2. Select **Settings** from the dropdown menu.

You'll see several sections: Account Information, Experience Mode, OpenAI API Key (if applicable), AI Model Settings, AI Services, and Subscription Management.

---

### 2. Update Account Information

**What you can change**:
- Email address
- Email verification status
- Password

#### Change Your Email

**For email/password accounts** (not Google sign-in):

1. In the **Account Information** section, next to your email, click **change**.
2. A modal opens:
   - Enter your **New Email**.
   - Enter your **Current Password** (for security).
3. Click **Update Email**.
4. You'll receive a verification email at your new address. Click the link to verify.

**For Google accounts**:
- Your email is managed by Google. Click **Managed by Google** to visit Google account settings.

#### Verify Your Email

If you see an **Unverified** badge next to your email:

1. Click **verify** next to your email.
2. Hi, Moose sends a verification link to your email.
3. Check your inbox and click the link.
4. Your email is now verified.

**Why verify?** Verified emails are required for some features (like team invitations) and improve account security.

#### Reset Your Password

**For email/password accounts**:

1. Next to **Password**, click **reset**.
2. A modal opens: Click **Send Password Reset Email**.
3. Check your inbox for a reset link from Firebase.
4. Click the link, enter a new password, and save.

**For Google accounts**:
- Your password is managed by Google. Click **Manage in Google** to update it there.

---

### 3. Choose Your Experience Mode

**What this does**: Adjusts the UI complexity across Hi, Moose. This is a personal preference—it doesn't change your subscription features.

#### Two Modes Available

- **Marketer Mode**:
  - Simplified interface.
  - Best for SMB marketers, content teams, or non-technical users.
  - Hides advanced SEO jargon and focuses on practical results.

- **SEO Mode**:
  - Full-featured interface.
  - Best for SEO professionals, agencies, or power users.
  - Shows advanced metrics, technical details, and pro-level options.

#### How to Switch Modes

1. In the **Experience Mode** section, you'll see two cards: **Marketer Mode** and **SEO Mode**.
2. Click the mode you want.
3. The selected mode is highlighted with a green or purple border and checkmark.
4. Your preference is saved automatically and applies immediately across the platform.

**Can I change this anytime?** Yes. Switch back and forth as often as you like—no restrictions.

---

### 4. Connect Your OpenAI API Key (BYOK Users Only)

**Who sees this section**: Users on the **BYOK (Bring Your Own Key)** plan only. If you're on Free, Starter, Growth, or Enterprise, skip this section.

#### Why Use BYOK?

- **No monthly token limits**: Use as much AI as you want—billed directly to your OpenAI account.
- **Cost control**: Pay only for what you use (OpenAI's per-token pricing).
- **Model flexibility**: Choose any OpenAI model (GPT-4.1, GPT-5, etc.).

#### How to Add Your API Key

1. In the **OpenAI API Key** section, you'll see:
   - A text field (hidden by default).
   - A **Test & Save** button.

2. Paste your OpenAI API key into the text field (starts with `sk-...`).
   - Click the **eye icon** to show/hide the key.

3. Click **Test & Save**.
   - Hi, Moose tests the key by making a simple API call to OpenAI.
   - If valid, the key is encrypted and saved to your account.
   - If invalid, you'll see an error. Check that the key is correct and active.

4. Once saved, the field shows `sk-••••••••••••••••••••••••••••••••••••••••••••••••••••••••` (masked).

**Get an OpenAI API key**: Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys), create an account, and generate a new key.

#### Update or Remove Your API Key

**To update**:
1. Paste a new key into the field.
2. Click **Test & Save**.
3. The old key is replaced.

**To remove**:
1. Click the **trash icon** (red button next to the field).
2. Confirm removal.
3. AI features will be disabled until you add a new key.

**Security note**: Your API key is **encrypted** before storage. It's never sent to the browser or exposed to other users—even your team members.

---

### 5. Select Your AI Model (BYOK Users Only)

**Who sees this section**: BYOK users only. If you're on a managed plan (Free, Starter, Growth, Enterprise), Hi, Moose automatically uses the best model for your tier.

#### Available Models

Hi, Moose supports 8 OpenAI models:
- **GPT-5, GPT-5 Mini, GPT-5 Nano**: Latest models (may return unexpected results for SEO tasks).
- **GPT-4.1, GPT-4.1 Mini, GPT-4.1 Nano**: Recommended for SEO tasks (most consistent results).
- **GPT-4o, GPT-4o Mini**: Optimized for speed and cost.

#### How to Select a Model

1. In the **AI Model Settings** section, you'll see 8 model cards.
2. Click the model you want to use.
3. The selected model is highlighted with a blue border and radio button.
4. Your preference is saved automatically.

**Recommendation**: Use **GPT-4.1** or **GPT-4.1 Mini** for SEO tasks. GPT-5 models are powerful but may produce inconsistent results for content optimization.

**Personal preference**: Your model selection applies only to your account. Team members must set their own models individually.

---

### 6. Monitor AI Token Usage (Managed Plans Only)

**Who sees this section**: Users on Free, Starter, Growth, or Enterprise plans. BYOK users don't have token limits (they pay per OpenAI usage).

#### What Are Tokens?

Tokens are units of AI usage. Every AI request (content generation, AEO analysis, etc.) consumes tokens based on:
- Input length (your prompt)
- Output length (AI response)
- Model used (GPT-4.1 uses more tokens than GPT-4o Mini)

Your plan includes a monthly token allowance. See [Plans](https://www.himoose.com/plans) for details.

#### How to Check Your Usage

1. In the **AI Services** section, you'll see an **AI Token Usage** box.
2. It shows:
   - **Used tokens**: How many you've consumed this month.
   - **Total tokens**: Your monthly limit.
   - **Percentage**: Visual progress bar (green = safe, yellow = 75%+, red = 90%+).

3. Usage resets on the **1st of each month**.

**Example**: `450,000 / 600,000 tokens` (75% used).

#### What Happens If I Run Out?

- AI features (content generation, AEO analysis, LLM Beacon checks) will stop working until:
  - Your usage resets next month.
  - You upgrade to a higher plan.
  - You switch to BYOK and use your own API key.

**Warning at 75%**: You'll see a yellow alert when you hit 75% usage.  
**Warning at 90%**: You'll see a red alert recommending an upgrade.

---

### 7. Manage Your Subscription

**Who sees this section**: Team owners only (not team members). If you're on the Free plan, you'll see upgrade options instead.

#### What You Can Do

- Update payment methods.
- Change billing cycle (monthly vs annual).
- Upgrade to a higher plan.
- Downgrade to a lower plan.
- Cancel your subscription.
- Reactivate a canceled subscription.

#### How to Manage

1. In the **Subscription Management** section, click **Manage Subscription**.
2. You're redirected to the **Stripe Customer Portal** (Hi, Moose's billing provider).
3. In the portal, you can:
   - Update your credit card.
   - Download invoices.
   - Change your plan.
   - Cancel or reactivate.

4. Changes take effect immediately or at the end of your current billing period (depending on the action).

#### Subscription Details

You'll see:
- **Current plan**: Your subscription tier (e.g., "Professional").
- **Next billing date**: When your card will be charged next.

If you've scheduled a cancellation or downgrade, you'll see a yellow warning:
- *"Your subscription will downgrade to Standard plan on [date]. Reactivate"*
- Click **Reactivate** to undo the cancellation.

---

### 8. Upgrade Your Plan (Free Users)

If you're on the **Free plan**, the **AI Services** section shows upgrade benefits:

**What you get with paid plans**:
- Improved AI quality & faster processing.
- Higher monthly token limits (up to 3,000,000 tokens on Enterprise).
- Access to LLM Beacon (track brand mentions in AI platforms).
- Advanced AEO optimization tools.
- Batch processing & Webflow sync.
- Brand voice & style guide control.

Click **View Upgrade Options** to see plan details and pricing.

---

## What You Get (Outputs)

After configuring settings, you have:

- **Personalized experience**: Marketer or SEO Mode to match your expertise.
- **Updated account info**: New email (verified), new password, or verified email status.
- **BYOK setup**: Your OpenAI API key connected and tested (if applicable).
- **AI model preference**: Your chosen GPT model (BYOK users only).
- **Usage visibility**: Clear view of monthly token consumption.
- **Subscription control**: Updated billing, plan changes, or cancellations.

Your settings apply immediately—no need to log out or refresh.

---

## Tips for Best Results

1. **Start with Marketer Mode**: If you're new to Hi, Moose or SEO, use Marketer Mode. It's less overwhelming. Switch to SEO Mode when you're comfortable.

2. **Verify your email**: Verified emails unlock team features and improve security. Do this early.

3. **BYOK users: Test your key first**: Click **Test & Save** before relying on your API key. If the test fails, check your OpenAI account for billing issues or key expiration.

4. **Use GPT-4.1 for SEO tasks**: GPT-5 is newer but less consistent for content optimization. Stick with GPT-4.1 or GPT-4.1 Mini (BYOK users).

5. **Monitor token usage weekly**: Check your usage mid-month (around the 15th) to avoid surprises. If you're at 50%+ by mid-month, consider upgrading.

6. **Upgrade before hitting limits**: Don't wait until you're at 100% tokens. Upgrade when you hit 75% to avoid interruptions.

7. **Team members: Set your own preferences**: Even if you're on a team, you can set your own Experience Mode and AI model (if BYOK). These are personal settings.

8. **BYOK cost control**: Set spending limits in your OpenAI account to avoid unexpected bills. Most Hi, Moose tasks use $0.01–$0.50 per request.

9. **Cancel wisely**: If you cancel your subscription, you'll lose access to paid features at the end of your billing period—not immediately. Use this time to export important data.

10. **Reactivate anytime**: Canceled your subscription by mistake? Click **Reactivate** in the Subscription Management section or visit the Stripe portal.

---

## Troubleshooting

### 1. "API key is invalid" error when testing OpenAI key

**Why**: Your OpenAI API key is incorrect, expired, or lacks permissions.

**Fix**:
- Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
- Verify the key is active (not revoked).
- Check your OpenAI account has sufficient funds (prepaid credits or payment method).
- Try regenerating the key and pasting the new one into Hi, Moose.

---

### 2. Email verification link not received

**Why**: The email is in your spam folder, or there was a delay.

**Fix**:
- Check your spam/junk folder.
- Wait 5 minutes and try clicking **verify** again.
- Add `noreply@himoose.com` to your email contacts.
- If still not received, contact [support@himoose.com](mailto:support@himoose.com).

---

### 3. "Update Email" fails—"Current password is incorrect"

**Why**: You entered the wrong password, or you're using Google sign-in (which doesn't use passwords).

**Fix**:
- If you're an email/password user: Double-check your password. Try resetting it if you've forgotten.
- If you're a Google user: Your email is managed by Google—you can't change it in Hi, Moose. Update it in your Google account instead.

---

### 4. Token usage shows "Loading..." and never updates

**Why**: Your account data isn't syncing, or there's a network issue.

**Fix**:
- Refresh the page (Ctrl+R or Cmd+R).
- Clear your browser cache and reload.
- If the issue persists, check your internet connection.
- Contact support if it's still broken after 10 minutes.

---

### 5. "Manage Subscription" button does nothing

**Why**: Your subscription portal session expired, or you're on the Free plan.

**Fix**:
- **Free users**: You don't have an active subscription—click **View Upgrade Options** instead.
- **Paid users**: Try clicking again. If it still doesn't work, log out and log back in.
- If redirected to Stripe but see an error, contact support with a screenshot.

---

### 6. Experience Mode doesn't change the UI

**Why**: You need to refresh the page, or the setting didn't save.

**Fix**:
- Refresh the page (Ctrl+R or Cmd+R).
- Click the mode again to confirm it's selected (checkmark appears).
- Clear your browser cache if the issue persists.
- Try a different browser (Chrome, Firefox, Safari).

---

### 7. AI features stopped working after adding BYOK key

**Why**: Your OpenAI account ran out of credits, or the key was revoked.

**Fix**:
- Go to [platform.openai.com/billing](https://platform.openai.com/account/billing) and check your balance.
- Add funds or a payment method.
- Verify the key is still active in your OpenAI dashboard.
- Test the key again in Settings → **Test & Save**.

---

### 8. Token usage shows 0 tokens used (but I've been using AI features)

**Why**: Usage data is delayed (can take 1–2 hours to sync).

**Fix**:
- Wait a few hours and check again.
- If it's been 24+ hours and still shows 0, contact support—there may be a tracking issue.

---

### 9. Can't remove BYOK API key—trash icon is grayed out

**Why**: You haven't added a key yet, or there's a UI bug.

**Fix**:
- The trash icon only appears if a key is already saved.
- If you see a masked key (`sk-••••••••`) but can't delete it, try refreshing the page.
- If the issue persists, contact support.

---

### 10. "Next billing date" shows a date 100 years in the future

**Why**: Stripe stores lifetime subscriptions with a far-future date. Hi, Moose auto-corrects this to show the actual next billing cycle.

**Fix**:
- This is intentional—ignore the year 2100+ date. Hi, Moose calculates the real billing date based on the month/day.
- If the corrected date still looks wrong, contact support.

---

## Frequently Asked Questions

### What's the difference between Marketer Mode and SEO Mode?

**Marketer Mode**:
- Simplified UI with less technical SEO jargon.
- Focuses on practical results (traffic, conversions, rankings).
- Best for small business owners, content marketers, or beginners.

**SEO Mode**:
- Full-featured UI with advanced metrics.
- Shows technical SEO details (crawl depth, entity recognition, grounding queries).
- Best for SEO professionals, agencies, or technical users.

**Both modes have the same features**—only the presentation changes.

---

### Can I use both Marketer and SEO Mode?

Not simultaneously—you pick one mode at a time. But you can switch back and forth anytime in Settings.

---

### Do team members see the same experience mode?

No. Experience Mode is **personal**—each user sets their own. Team members can use Marketer Mode while the owner uses SEO Mode.

---

### What happens if I cancel my subscription?

- You'll keep access to paid features until the end of your current billing period.
- After that, you're downgraded to Free (or the tier you selected).
- Your projects, data, and content are preserved—you just lose access to premium features (AI generation, LLM Beacon, etc.).

You can reactivate anytime by clicking **Manage Subscription** → **Reactivate**.

---

### Can I change my email if I signed up with Google?

No. Google-managed emails are tied to your Google account. To change it:
1. Go to [myaccount.google.com](https://myaccount.google.com).
2. Update your primary email there.
3. Log out of Hi, Moose and log back in with the new email.

---

### How do I know if I'm on a team plan?

If you're a team member:
- You'll see a **Team Plan** badge next to your plan name in Settings.
- The **Subscription Management** section will say: *"You're currently part of a team on the [Plan Name] plan. Contact your team owner to discuss plan changes."*

Team owners don't see this badge—they see the full subscription controls.

---

### What's BYOK and should I use it?

**BYOK (Bring Your Own Key)** means you connect your own OpenAI API key instead of using Hi, Moose's managed AI.

**Pros**:
- No monthly token limits.
- You control costs (pay OpenAI directly).
- Choose any GPT model.

**Cons**:
- Requires an OpenAI account and billing setup.
- You're responsible for managing API costs.
- No managed support if OpenAI has issues.

**Who should use BYOK**:
- High-volume users (agencies, enterprises).
- Users who want GPT-5 or specific models.
- Users who prefer pay-as-you-go pricing.

**Who shouldn't use BYOK**:
- Beginners or low-volume users (managed plans are simpler).
- Users who want predictable monthly pricing.

---

### How much does BYOK cost?

BYOK plans have a small monthly fee (varies by tier), plus your OpenAI usage costs.

**OpenAI pricing** (as of Dec 2024):
- GPT-4.1: ~$0.03 per 1,000 input tokens, ~$0.06 per 1,000 output tokens.
- GPT-4.1 Mini: ~$0.015 per 1,000 tokens (cheaper).
- GPT-5: ~$0.05+ per 1,000 tokens (most expensive).

**Example**: Generating 50 content briefs might use 250,000 tokens ≈ $7.50 (GPT-4.1).

See [Plans](https://www.himoose.com/plans) for BYOK monthly fees.

---

### Can I switch from managed AI to BYOK (or vice versa)?

Yes. Go to **Plans** and select a different tier. You can switch anytime—changes take effect at the end of your billing period.

**From managed to BYOK**: You'll need to add your OpenAI API key in Settings before AI features work.

**From BYOK to managed**: Your OpenAI key is removed, and Hi, Moose's AI takes over.

---

### Why does my token usage reset on the 1st of the month?

All Hi, Moose plans have **monthly billing cycles** that reset on the 1st. This keeps usage tracking consistent for all users.

If you signed up mid-month, you still get your full monthly allocation immediately (not prorated).

---

### What models do managed plans use?

- **Free**: Lower-tier models (slower, less accurate).
- **Starter (Bronze)**: GPT-4.1 Mini.
- **Growth (Silver)**: GPT-4.1.
- **Enterprise (Gold)**: GPT-4.1 (optimized for speed).

Hi, Moose automatically selects the best model for your tier—you can't change it on managed plans. Switch to BYOK if you want model control.

---

### Can I see my team's token usage?

**Team owners**: Yes. Go to **Admin Dashboard** (if you're on a paid team plan) to see aggregate usage.

**Team members**: No. You only see your personal usage. Ask your team owner for team-wide stats.

---

### What happens to my data if I downgrade or cancel?

- Your **projects, data, and content are preserved** for 90 days after downgrading to Free or canceling.
- You can still access and export your data during this time.
- After 90 days of inactivity, archived data may be deleted (per our data retention policy).

**Recommendation**: Export important data (CSV, Webflow, etc.) before canceling.

---

### How do I export my data before canceling?

- **Content Briefs**: Copy/paste content or use Webflow export.
- **AEO Reports**: Take screenshots or save as PDF (browser print).
- **LLM Beacon Reports**: Export to CSV (available in the feature).
- **Versus Pages**: Export to CSV (Step 7 in wizard).
- **Projects**: No bulk export—export feature-by-feature.

---

### Can I upgrade mid-month?

Yes. When you upgrade:
- You're charged the prorated difference immediately.
- Your new limits (tokens, features) take effect instantly.
- Your billing date stays the same.

**Example**: Upgrade from Starter ($49/mo) to Growth ($99/mo) on the 15th. You're charged ~$25 (half the difference) immediately.

---

### Can I pause my subscription?

No. Hi, Moose doesn't support pausing. You can:
- **Cancel** (keeps access until period end, then downgrades to Free).
- **Downgrade** to a cheaper plan (e.g., Growth → Starter).

If you need a temporary break, cancel and reactivate when you're ready.

---

### Why does "Manage Subscription" open a Stripe page?

Hi, Moose uses **Stripe** for payment processing (industry-standard, PCI-compliant). The Stripe Customer Portal lets you:
- Update payment methods securely.
- View invoices.
- Change plans.
- Cancel subscriptions.

Your data is encrypted and never stored on Hi, Moose's servers—only Stripe has your payment info.

---

## Related Features

- **Plans**: See all subscription tiers and pricing. Visit [Plans Page](https://www.himoose.com/plans).
- **Admin Dashboard**: Team owners can manage team members, view usage, and control permissions (paid plans only).
- **Projects**: Organize your work into projects with custom settings. See [How to Manage Projects](#).

---

**Still stuck?** Check the [Support](https://www.himoose.com/contact) page or email support@himoose.com. Include a screenshot of the Settings page for faster help.
