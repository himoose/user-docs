# Hi, Moose Documentation Site

Public user documentation for Hi, Moose - AI search optimization platform.

This documentation site is built with **MkDocs**, deployed to **Firebase Hosting**, and served at `himoose.com/docs` via a **Cloudflare Worker**.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+ (for Firebase CLI)
- Firebase account
- Cloudflare account with domain access

### Local Development

1. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

2. **Serve documentation locally:**

```bash
mkdocs serve
```

The site will be available at `http://localhost:8000`

3. **Build static site:**

```bash
mkdocs build
```

This generates static files in the `site/` directory.

## 📁 Project Structure

```
user-docs/
├── docs/                          # Markdown documentation files
│   ├── index.md                  # Homepage
│   ├── getting-started/
│   │   ├── introduction.md
│   │   ├── quick-start.md
│   │   └── installation.md
│   ├── user-guide/
│   │   ├── overview.md
│   │   ├── features.md
│   │   └── best-practices.md
│   ├── search-optimization/
│   │   ├── seo-basics.md
│   │   └── ai-integration.md
│   ├── faq.md
│   └── support.md
├── src/
│   └── index.js                  # Cloudflare Worker script
├── mkdocs.yml                    # MkDocs configuration
├── requirements.txt              # Python dependencies
├── firebase.json                 # Firebase Hosting config
├── .firebaserc                   # Firebase project config
├── wrangler.toml                # Cloudflare Worker config
└── README.md                     # This file
```

## 🎨 Customization

### Update Navigation

Edit [mkdocs.yml](mkdocs.yml) to modify the navigation structure:

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Introduction: getting-started/introduction.md
  # Add more sections...
```

### Theme Configuration

The site uses Material for MkDocs. Customize colors, fonts, and features in [mkdocs.yml](mkdocs.yml):

```yaml
theme:
  name: material
  palette:
    primary: indigo
    accent: indigo
```

### Add New Pages

1. Create a new `.md` file in the `docs/` directory
2. Add it to the navigation in `mkdocs.yml`
3. Preview changes with `mkdocs serve`

## 🔥 Firebase Deployment

### Initial Setup

1. **Install Firebase CLI:**

```bash
npm install -g firebase-tools
```

2. **Login to Firebase:**

```bash
firebase login
```

3. **Initialize Firebase (if not already done):**

```bash
firebase init hosting
```

- Select your Firebase project (or create new one)
- Set public directory to: `site`
- Configure as single-page app: `No`
- Don't overwrite existing files

4. **Update `.firebaserc` with your project ID:**

```json
{
  "projects": {
    "default": "your-firebase-project-id"
  }
}
```

### Deploy to Firebase

1. **Build the documentation:**

```bash
mkdocs build
```

2. **Deploy to Firebase:**

```bash
firebase deploy
```

Your docs will be available at: `https://your-project-id.web.app`

### Automated Deployment

For CI/CD, use GitHub Actions:

```yaml
name: Deploy Docs

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Build docs
        run: mkdocs build
      
      - name: Deploy to Firebase
        uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          projectId: your-firebase-project-id
```

## ☁️ Cloudflare Worker Setup

The Cloudflare Worker routes requests from `himoose.com/docs` to your Firebase Hosting.

### Setup Steps

1. **Install Wrangler CLI:**

```bash
npm install -g wrangler
```

2. **Login to Cloudflare:**

```bash
wrangler login
```

3. **Update wrangler.toml:**

Replace `YOUR_CLOUDFLARE_ACCOUNT_ID` and `FIREBASE_HOSTING_URL` with your values:

```toml
account_id = "your-cloudflare-account-id"

[env.production]
vars = { FIREBASE_HOSTING_URL = "https://your-project.web.app" }
```

4. **Deploy the Worker:**

```bash
wrangler deploy
```

5. **Configure Routes in Cloudflare Dashboard:**

- Go to your Cloudflare dashboard
- Navigate to Workers & Pages → your worker
- Add routes:
  - `himoose.com/docs`
  - `himoose.com/docs/*`

### Testing the Worker

Test locally with:

```bash
wrangler dev
```

Visit `http://localhost:8787/docs` to test the routing.

## 🔄 Complete Deployment Workflow

Here's the complete process from local development to production:

### 1. Local Development & Testing

```bash
# Serve docs locally
mkdocs serve

# Make changes to markdown files
# Preview at http://localhost:8000
```

### 2. Build & Test

```bash
# Build static site
mkdocs build

# Test the built site
cd site && python -m http.server 8000
```

### 3. Deploy to Firebase

```bash
# Deploy to Firebase Hosting
firebase deploy

# Test at: https://your-project.web.app
```

### 4. Deploy Cloudflare Worker

```bash
# Deploy worker
wrangler deploy

# Test at: https://himoose.com/docs
```

### 5. Verify

Visit `https://himoose.com/docs` and verify:
- All pages load correctly
- Navigation works
- Links are correct
- Images display
- Search functionality works

## 📝 Content Guidelines

### Writing Documentation

- Use clear, concise language
- Include examples where appropriate
- Add code blocks with syntax highlighting
- Use admonitions for tips, warnings, notes
- Keep paragraphs short (3-4 sentences)
- Use bullet points for lists
- Include screenshots when helpful

### Markdown Tips

**Admonitions:**

```markdown
!!! tip "Pro Tip"
    This is a helpful tip for users.

!!! warning "Important"
    This is something users should be careful about.

!!! note
    This is additional information.
```

**Code Blocks:**

````markdown
```python
# Python code example
def hello_world():
    print("Hello, World!")
```
````

**Links:**

```markdown
[Link text](page-name.md)
[External link](https://example.com)
```

## 🧪 Testing

### Test Locally

```bash
# Serve and test
mkdocs serve

# Build and check for errors
mkdocs build --strict
```

### Check for Broken Links

Install and use linkchecker:

```bash
pip install linkchecker
mkdocs serve &
linkchecker http://localhost:8000
```

## 🐛 Troubleshooting

### MkDocs Issues

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**Theme not loading:**
```bash
pip install --upgrade mkdocs-material
```

### Firebase Issues

**Authentication error:**
```bash
firebase login --reauth
```

**Wrong project:**
```bash
firebase use your-project-id
```

### Cloudflare Worker Issues

**Routes not working:**
- Check route configuration in Cloudflare dashboard
- Ensure worker is deployed to production
- Verify environment variables are set

**CORS errors:**
- Check Firebase Hosting CORS configuration
- Verify worker headers

## 📚 Additional Resources

### MkDocs Documentation
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Python Markdown Extensions](https://python-markdown.github.io/extensions/)

### Firebase Hosting
- [Firebase Hosting Docs](https://firebase.google.com/docs/hosting)
- [Firebase CLI Reference](https://firebase.google.com/docs/cli)

### Cloudflare Workers
- [Workers Documentation](https://developers.cloudflare.com/workers/)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)

## 🤝 Contributing

### Making Updates

1. Create a new branch for your changes
2. Update markdown files in `docs/`
3. Test locally with `mkdocs serve`
4. Build and verify: `mkdocs build --strict`
5. Commit and push changes
6. Deploy to Firebase
7. Deploy Cloudflare Worker (if needed)

### Content Review Process

1. Technical accuracy check
2. Grammar and spelling review
3. Link verification
4. Screenshot updates (if needed)
5. Final preview before deployment

## 📞 Support

For questions or issues:

- **Documentation Issues**: Open an issue in the repository
- **Technical Support**: support@himoose.com
- **General Questions**: Check the [FAQ](docs/faq.md)

## 📄 License

Copyright © 2025 Hi, Moose. All rights reserved.

---

## Quick Reference Commands

```bash
# Local development
mkdocs serve                  # Serve locally
mkdocs build                  # Build static site
mkdocs build --strict         # Build with strict error checking

# Firebase
firebase login                # Login to Firebase
firebase init                 # Initialize Firebase
firebase deploy               # Deploy to Firebase
firebase serve                # Test Firebase locally

# Cloudflare Worker
wrangler login                # Login to Cloudflare
wrangler dev                  # Test worker locally
wrangler deploy               # Deploy worker
wrangler tail                 # View worker logs

# Useful development commands
pip install -r requirements.txt    # Install Python dependencies
pip list                          # List installed packages
python -m http.server 8000        # Simple HTTP server
```

---

Made with ❤️ by the Hi, Moose team
