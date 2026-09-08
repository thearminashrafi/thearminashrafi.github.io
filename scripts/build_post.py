#!/usr/bin/env python3
"""Turn a Markdown post in posts/ into a real page in blogs/, and register
it in blogs/index.html.

Usage:
  python3 scripts/build_post.py my-post-slug     # build one post
  python3 scripts/build_post.py --all            # rebuild every post

Safe to re-run: it regenerates blogs/<slug>.html from posts/<slug>.md every
time, and updates (rather than duplicates) the post's entry in
blogs/index.html if it already exists there. Only the .md file in posts/
is meant to be hand-edited — the generated .html file in blogs/ is
overwritten on every build.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
BLOGS = ROOT / "blogs"
TEMPLATE = BLOGS / "template.html"
INDEX = BLOGS / "index.html"

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


def parse_post(md_path: Path):
    text = md_path.read_text()
    m = FRONT_MATTER_RE.match(text)
    if not m:
        sys.exit(
            f"{md_path} doesn't start with a '---' front-matter header. "
            "Expected:\n---\ntitle: ...\ndate: ...\nexcerpt: ...\nread: ...\n---\n<post body>"
        )
    header_text, body = m.groups()

    fields = {}
    for line in header_text.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            sys.exit(f"Couldn't parse front-matter line in {md_path}: {line!r}")
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()

    missing = [k for k in ("title", "date", "excerpt", "read") if k not in fields]
    if missing:
        sys.exit(f"{md_path} front matter is missing: {', '.join(missing)}")

    fields["read"] = int(fields["read"])
    fields["body"] = body.strip("\n")
    return fields


def display_date(iso_date: str) -> str:
    import datetime
    d = datetime.date.fromisoformat(iso_date)
    day = str(d.day)  # no leading zero, cross-platform
    return d.strftime(f"%b {day}, %Y")


def render_html(slug: str, fields: dict) -> str:
    template_text = TEMPLATE.read_text()

    # Drop the "HOW TO USE THIS TEMPLATE" instructions comment — it's for
    # someone editing the template by hand, not relevant to a built page.
    howto_start = "  <!--\n  ─── HOW TO USE THIS TEMPLATE"
    howto_end_marker = "──── -->\n"
    if howto_start in template_text:
        s = template_text.index(howto_start)
        e = template_text.index(howto_end_marker, s) + len(howto_end_marker)
        template_text = template_text[:s] + template_text[e:]

    start_marker = "  <!-- Option B: Markdown content — uncomment and fill in -->"
    end_marker = "\n  -->\n"
    start_idx = template_text.index(start_marker)
    end_idx = template_text.index(end_marker, start_idx) + len(end_marker)

    body = fields["body"].replace("</script>", "<\\/script>")
    md_block = (
        "  <script id=\"md-content\" type=\"text/markdown\">\n"
        f"{body}\n"
        "  </script>\n"
    )
    html = template_text[:start_idx] + md_block + template_text[end_idx:]

    html = html.replace("[Post Title] — Armin Ashrafi", f"{fields['title']} — Armin Ashrafi")
    html = html.replace('content="[One-sentence summary]"', f'content="{fields["excerpt"]}"')
    html = html.replace(">[Post Title]<", f">{fields['title']}<")
    html = html.replace("[Month DD, YYYY]", display_date(fields["date"]))
    html = html.replace("[X] min read", f"{fields['read']} min read")
    return html


def upsert_index_entry(slug: str, fields: dict):
    index_text = INDEX.read_text()
    href = f"{slug}.html"

    entry = (
        "    {\n"
        f"      title:   {json.dumps(fields['title'])},\n"
        f"      date:    {json.dumps(fields['date'])},\n"
        f"      display: {json.dumps(display_date(fields['date']))},\n"
        f"      excerpt: {json.dumps(fields['excerpt'])},\n"
        f"      read:    {int(fields['read'])},\n"
        f"      href:    {json.dumps(href)}\n"
        "    },\n"
    )

    # Remove any existing entry for this href, so re-building a post updates
    # it in place instead of creating a duplicate.
    existing_entry_re = re.compile(
        r"[ \t]*\{\s*title:.*?href:\s*" + re.escape(json.dumps(href)) + r"\s*\},?\n",
        re.DOTALL,
    )
    index_text = existing_entry_re.sub("", index_text)

    marker = "const posts = ["
    idx = index_text.index(marker) + len(marker)
    rest = index_text[idx:].lstrip()
    if rest.startswith("]"):
        new_text = index_text[:idx] + "\n" + entry + "  " + rest
    else:
        new_text = index_text[:idx] + "\n" + entry + index_text[idx:]

    INDEX.write_text(new_text)


def build_one(md_path: Path):
    slug = md_path.stem
    fields = parse_post(md_path)
    html = render_html(slug, fields)
    out_path = BLOGS / f"{slug}.html"
    out_path.write_text(html)
    upsert_index_entry(slug, fields)
    print(f"Built {out_path.relative_to(ROOT)}  (from {md_path.relative_to(ROOT)})")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    if sys.argv[1] == "--all":
        md_files = sorted(POSTS.glob("*.md"))
        if not md_files:
            sys.exit(f"No .md files found in {POSTS.relative_to(ROOT)}/")
        for md_path in md_files:
            build_one(md_path)
    else:
        slug = sys.argv[1]
        if slug.endswith(".md"):
            slug = slug[: -len(".md")]
        md_path = POSTS / f"{slug}.md"
        if not md_path.exists():
            sys.exit(f"{md_path} not found. Run scripts/new_post.py first.")
        build_one(md_path)

    print("\nNext: git add posts/ blogs/ && git commit -m \"...\" && git push origin main")


if __name__ == "__main__":
    main()
