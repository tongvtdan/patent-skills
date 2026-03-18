#!/usr/bin/env python3
"""
Push patent-skills files to GitHub.
Run this whenever you update a skill file.

Usage:
  python3 push_to_github.py                    # push all files
  python3 push_to_github.py skills/patent-research/SKILL.md  # push one file
"""
import os, base64, json, urllib.request, urllib.error, sys

TOKEN = os.environ.get("GITHUB_TOKEN", "")  # set via: export GITHUB_TOKEN=ghp_...
if not TOKEN:
    print("❌ Set GITHUB_TOKEN env var first:  export GITHUB_TOKEN=ghp_...")
    print("   Generate at: https://github.com/settings/tokens (repo scope, 30 days)")
    sys.exit(1)
REPO  = "tongvtdan/patent-skills"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def push_file(rel_path, full_path):
    with open(full_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    url = f"https://api.github.com/repos/{REPO}/contents/{rel_path}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    # Get existing file SHA (required for updates, not creates)
    sha = None
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as r:
            sha = json.loads(r.read()).get("sha")
    except urllib.error.HTTPError:
        pass  # File doesn't exist yet — first push

    payload = {"message": f"Update {rel_path}", "content": content}
    if sha:
        payload["sha"] = sha

    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as r:
            result = json.loads(r.read())
            action = "Updated" if sha else "Created"
            return f"✅ {action}: {rel_path}"
    except urllib.error.HTTPError as e:
        return f"❌ Failed {rel_path}: {e.code} — {e.read().decode()[:120]}"

# ── Main ────────────────────────────────────────────────────────────────────

if len(sys.argv) > 1:
    # Push specific file(s)
    for arg in sys.argv[1:]:
        full_path = os.path.join(BASE_DIR, arg)
        print(push_file(arg, full_path))
else:
    # Push all files
    pushed = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fname in sorted(files):
            if fname == "push_to_github.py":
                continue  # skip self
            full_path = os.path.join(root, fname)
            rel_path  = os.path.relpath(full_path, BASE_DIR)
            print(push_file(rel_path, full_path))
            pushed += 1
    print(f"\n{pushed} files synced to github.com/{REPO}")
