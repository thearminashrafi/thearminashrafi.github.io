#!/usr/bin/env python3
"""Scaffold a new blog post: copies the template, fills in the header,
and registers it in blogs/index.html's posts[] array.

Usage:
  python3 scripts/new_post.py "My Post Title"
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOGS = ROOT / "blogs"
TEMPLATE = BLOGS / "template.html"
INDEX = BLOGS / "index.html"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def main():
    if len(sys.argv) < 2:
        title = input("Post title: ").strip()
    else:
        title = " ".join(sys.argv[1:]).strip()
    if not title:
        sys.exit("A title is required.")

    slug = slugify(title)
    post_path = BLOGS / f"{slug}.html"
    if post_path.exists():
        sys.exit(f"{post_path} already exists — pick a different title or delete it first.")

    excerpt = input("One-sentence excerpt (shown in the listing): ").strip()
    if not excerpt:
        excerpt = "TODO: write an excerpt."

    read = input("Estimated read time in minutes [5]: ").strip() or "5"

    today = datetime.date.today()
    iso_date = today.isoformat()
    display_date = today.strftime("%b %-d, %Y") if sys.platform != "win32" else today.strftime("%b %d, %Y")

    # --- Write the post file from the template ---
    text = TEMPLATE.read_text()
    text = text.replace("[Post Title] — Armin Ashrafi", f"{title} — Armin Ashrafi")
    text = text.replace('content="[One-sentence summary]"', f'content="{excerpt}"')
    text = text.replace(">[Post Title]<", f">{title}<")
    text = text.replace("[Month DD, YYYY]", display_date)
    text = text.replace("[X] min read", f"{read} min read")
    post_path.write_text(text)

    # --- Register the post in blogs/index.html ---
    index_text = INDEX.read_text()
    entry = (
        "    {\n"
        f'      title:   {json.dumps(title)},\n'
        f'      date:    {json.dumps(iso_date)},\n'
        f'      display: {json.dumps(display_date)},\n'
        f'      excerpt: {json.dumps(excerpt)},\n'
        f'      read:    {int(read)},\n'
        f'      href:    {json.dumps(slug + ".html")}\n'
        "    },\n"
    )
    marker = "const posts = ["
    idx = index_text.index(marker) + len(marker)
    # Insert as the first element; empty-array case (posts = []) still works.
    rest = index_text[idx:].lstrip()
    if rest.startswith("]"):
        new_text = index_text[:idx] + "\n" + entry + "  " + rest
    else:
        new_text = index_text[:idx] + "\n" + entry + index_text[idx:]
    INDEX.write_text(new_text)

    print(f"\nCreated {post_path.relative_to(ROOT)}")
    print(f"Registered in {INDEX.relative_to(ROOT)}")
    print(f"\nNext: open {post_path.relative_to(ROOT)} and write your content")
    print("(inside <article id=\"prose-content\">, or uncomment the Markdown <script> block).")


if __name__ == "__main__":
    main()
