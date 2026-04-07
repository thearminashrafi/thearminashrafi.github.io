#!/usr/bin/env python3
"""Run from repo root: python3 wiki/build-manifest.py"""
import json, re
from pathlib import Path

wiki_dir = Path(__file__).parent
entries = []

EXCLUDE_DIRS = {'.obsidian', 'templates'}

for md_file in sorted(wiki_dir.glob('**/*.md')):
    if any(part in EXCLUDE_DIRS for part in md_file.parts):
        continue

    rel = str(md_file.relative_to(wiki_dir))
    text = md_file.read_text(encoding='utf-8')

    title = md_file.stem.replace('-', ' ').replace('_', ' ').title()
    tags, date, content = [], '', text

    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            fm, content = text[3:end], text[end + 4:].strip()
            in_tags = False
            for line in fm.splitlines():
                if line.startswith('title:'):
                    title = line[6:].strip().strip('"\''); in_tags = False
                elif line.startswith('date:'):
                    date = line[5:].strip(); in_tags = False
                elif line.startswith('tags:'):
                    val = line[5:].strip()
                    if val.startswith('['):
                        tags = [t.strip().strip('"\'') for t in val.strip('[]').split(',') if t.strip()]
                        in_tags = False
                    else:
                        in_tags = True
                elif in_tags and re.match(r'^\s*-\s+', line):
                    tags.append(re.sub(r'^\s*-\s+', '', line).strip())
                elif in_tags and line and not line.startswith(' '):
                    in_tags = False

    excerpt = next(
        (re.sub(r'[*_`\[\]#>]', '', l.strip())[:200]
         for l in content.splitlines()
         if l.strip() and not l.strip().startswith(('#', '!', '---'))),
        ''
    )

    entries.append({'path': rel, 'title': title, 'tags': tags,
                    'date': str(date), 'excerpt': excerpt, 'content': content})

entries.sort(key=lambda x: x['date'] or '0000', reverse=True)

(wiki_dir / 'manifest.json').write_text(
    json.dumps(entries, indent=2, ensure_ascii=False))

(wiki_dir / 'manifest.js').write_text(
    'window.__WIKI_MANIFEST__ = ' + json.dumps(entries, ensure_ascii=False) + ';\n')

print(f"Done — {len(entries)} notes written to manifest.js")
