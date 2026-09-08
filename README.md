# thearminashrafi.github.io

Personal academic website — plain HTML/CSS/JS, hosted on GitHub Pages, no build step.

---

## First-time setup

**Prerequisites:** Git.

```bash
# Clone the repo
git clone https://github.com/thearminashrafi/thearminashrafi.github.io.git
cd thearminashrafi.github.io
```

**Enable GitHub Pages** (one time, on GitHub):

1. Go to the repo → **Settings** → **Pages**
2. Source: **GitHub Actions** (required — the deploy workflow builds the site, including `/wiki`)
3. Push to `main` — the site goes live at `https://thearminashrafi.github.io` within a minute or two

---

## Site Structure

```
├── index.html          # Home — profile, bio, and publications
├── contact.html        # Contact
├── styles.css          # Shared styles (edit this to change colors/fonts)
│
└── assets/             # Images, PDFs
```

---

## Research — Adding a publication

In `index.html`, find the `.pub-list` block and copy an existing `.pub-entry` div,
updating the title, authors, venue, links, thumbnail, abstract, and BibTeX.

Then push:

```bash
git add index.html
git commit -m "research: add publication on ..."
git push origin main
```

---

## Pushing other changes

For any edits (HTML pages, styles, assets):

```bash
git add <files>
git commit -m "describe what changed"
git pull --rebase origin main   # pull first to avoid conflicts
git push origin main
```

---

## Cheatsheet

| Task | What to do |
|---|---|
| Add/edit a note | Write in Obsidian under `wiki/` → `git add wiki/` → `git push` |
| Add a publication | Copy a `.pub-entry` block in `index.html` → `.pub-list`, `git push` |
| Update bio / photo | Edit `index.html` → `.research-intro` section; replace `assets/armin.jpg` |
| Change accent color | Edit `--accent` in `styles.css` |
| Change contact email | Edit `contact.html` → `emailBtn` click handler |
| Update CV | Replace `assets/Resume_PhD.pdf` |

---

## Notes (Quartz)

Your Obsidian vault at `wiki/` is published at `https://thearminashrafi.github.io/wiki/` using
[Quartz](https://quartz.jzhao.xyz/). `wiki/` is your live Obsidian vault (open it directly in Obsidian) —
only `wiki/.obsidian/` (Obsidian's local app settings) is excluded from git; everything else you write
there gets published.

### How it works

- `quartz/` is a self-contained Quartz project (its own `package.json`, ignored `node_modules/`).
- `quartz/content` is a symlink to `../wiki`, so Quartz always reads your current notes — nothing to sync by hand.
- A GitHub Actions workflow (`.github/workflows/deploy.yml`) builds Quartz from `wiki/` and combines it
  with the rest of this site (`index.html`, `contact.html`, etc.) into `/wiki` on every push to `main`.
- The site nav's "Notes" link (`index.html`, `contact.html`) points at `wiki/`.
- Display math (`$$...$$`) is auto-normalized at build time by
  `quartz/local-plugins/fix-display-math` — write it however you like in
  Obsidian (single line or fenced), it always renders in proper KaTeX
  display mode on the site.

### Keeping the main site and notes theme in sync

`styles.css` (main site) and `quartz/quartz.config.yaml`'s `theme.colors`/
`theme.typography` (notes) are two **separate, manually-synced** palettes —
not one shared source of truth. If you change one site's colors or fonts
(light or dark), update the other to match by hand, or the two halves of
the site will visually drift apart. Also note `theme.typography` alone
isn't enough for the notes site: the `@quartz-community/quartz-fonts`
plugin needs its own matching `body`/`header`/`code` options (see the
comment above that plugin's config) or it silently falls back to Quartz's
stock fonts regardless of `theme.typography`.

### Publishing notes

Just write in Obsidian, then:

```bash
git add wiki/
git commit -m "notes: <what changed>"
git push origin main
```

GitHub Actions rebuilds and redeploys automatically — check the **Actions** tab on GitHub for progress.
The site updates within a couple of minutes at `https://thearminashrafi.github.io/wiki/`.

### Excluding a note from publishing

Add `private: true` to a note's YAML frontmatter, e.g.:

```
---
private: true
---
```

or add its folder name to `ignorePatterns` in `quartz/quartz.config.yaml`.

### Previewing locally

```bash
cd quartz
npx quartz build --serve
```

then open the printed `localhost` URL.

### One-time setup

This repo's GitHub Pages source must be set to **GitHub Actions** rather than "Deploy from a branch":
repo → **Settings** → **Pages** → **Source** → **GitHub Actions**. Until this is switched, pushes will
not publish `/wiki` (or the rest of the site via the new workflow).
