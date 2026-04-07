#!/bin/bash
# wiki-sync.sh — rebuild the wiki manifest, pull remote changes, and push.
# Run from the repo root: ./wiki-sync.sh

set -e  # exit immediately if any command fails

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo ""
echo "── Wiki Sync ────────────────────────────────────────"

# ── 1. Rebuild manifest ───────────────────────────────────
echo "▶ Rebuilding wiki manifest..."
python3 wiki/build-manifest.py

# ── 2. Stage all wiki changes ─────────────────────────────
echo "▶ Staging changes..."
git add wiki/

# Check if there's actually anything new to commit
if git diff --cached --quiet; then
  echo "  No wiki changes to commit."
else
  # Build a commit message listing which notes changed
  CHANGED=$(git diff --cached --name-only | grep '\.md$' | sed 's|wiki/||' | tr '\n' ', ' | sed 's/,$//')
  if [ -z "$CHANGED" ]; then
    MSG="wiki: update manifest"
  else
    MSG="wiki: update notes — $CHANGED"
  fi

  git commit -m "$MSG

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
  echo "  Committed: $MSG"
fi

# ── 3. Pull remote changes (rebase to keep history clean) ─
echo "▶ Pulling remote changes..."
git pull --rebase origin main

# ── 4. Push ───────────────────────────────────────────────
echo "▶ Pushing to origin..."
git push origin main

echo ""
echo "✓ Done — wiki is live."
echo "────────────────────────────────────────────────────"
echo ""
