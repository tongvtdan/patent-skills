# How to Publish & Install Patent Skills

## Step 1 — Create the GitHub Repo

1. Go to [github.com/new](https://github.com/new)
2. Set:
   - **Repository name**: `patent-skills`
   - **Visibility**: Public ← required for Cowork marketplace install
   - **Description**: Patent and IP skills for inventors and entrepreneurs (Vietnam + PCT + USPTO)
   - Do NOT check "Add README" — we already have one
3. Click **Create repository**

## Step 2 — Push the Files

Copy and run these commands in your terminal from the `patent-skills-repo` folder:

```bash
cd "path/to/Skill-builder/patent-skills-repo"

git branch -m main
git remote add origin https://github.com/YOUR_USERNAME/patent-skills.git
git commit -m "Initial release: patent-skills v1.0.0"
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 3 — Update Your Username in Two Files

Before pushing, update your GitHub username in:

**`.claude-plugin/marketplace.json`** — change the `owner.url`:
```json
"url": "https://github.com/YOUR_USERNAME"
```

**`patent-skills/.claude-plugin/plugin.json`** — change the `author.url`:
```json
"url": "https://github.com/YOUR_USERNAME/patent-skills"
```

**`README.md`** — update the installation URL:
```markdown
Enter the GitHub repo URL: `https://github.com/YOUR_USERNAME/patent-skills`
```

## Step 4 — Install in Claude Cowork

1. Open **Claude desktop app**
2. Go to **Settings → Plugins**
3. Click **Add Marketplace** (or **Add Plugin Source**)
4. Enter your repo URL: `https://github.com/YOUR_USERNAME/patent-skills`
5. Click **Connect**
6. Find **patent-skills** in the list → click **Install**
7. Start a **new chat** — the commands are now live

## Step 5 — Test It

Try these in a new chat:

```
/patent-skills:file-patent
```
→ Starts the guided filing workflow

```
/patent-skills:search-prior-art biodegradable packaging from agricultural waste
```
→ Runs prior art search + patentability assessment

```
/patent-skills:build-ip-strategy Vietnamese startup, 3 inventions, raising seed round
```
→ Builds full IP strategy

```
/patent-skills:respond-to-rejection
```
→ Helps draft office action response

---

## Troubleshooting

**Commands not showing?**
→ Make sure the repo is **Public** (private repos aren't discoverable as marketplaces)
→ Restart Claude after installation

**"Invalid marketplace" error?**
→ Check that `.claude-plugin/marketplace.json` exists at the root of the repo
→ Verify the JSON is valid (no trailing commas)

**Skills not triggering automatically?**
→ Skills auto-trigger when your phrasing matches their description
→ Try more specific language: "search prior art for X" vs. just "X"
→ Or force it: `/patent-skills:search-prior-art your invention here`
