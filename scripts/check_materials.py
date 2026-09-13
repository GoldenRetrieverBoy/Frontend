"""Check local Markdown navigation, permanent IDs, coverage and progress."""
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
files = sorted(root.rglob('*.md'))
texts = {p.resolve(): p.read_text(encoding='utf-8') for p in files if '.git' not in p.parts}
errors = []
ids = []
for path, text in texts.items():
    # Code examples may contain Markdown-looking text; exclude fenced blocks.
    body = re.sub(r'```.*?```', '', text, flags=re.S)
    for ident in re.findall(r'^## ([A-Z]+-\d+)\.', body, re.M):
        ids.append(ident)
        if f'<a id="{ident.lower()}"></a>' not in body:
            errors.append(f'{path.relative_to(root)}: missing anchor for {ident}')
    if path.name != 'progress.md' and re.search(r'^\s*- \[[ x~]\]', body, re.M):
        errors.append(f'{path.relative_to(root)}: progress checkbox outside journal')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        relative, _, fragment = unquote(target).partition('#')
        resolved = (path.parent / relative).resolve() if relative else path
        if not resolved.exists():
            errors.append(f'{path.relative_to(root)}: missing {target}')
        elif fragment:
            destination = texts.get(resolved, '')
            explicit = set(re.findall(r'<a id="([^"]+)"', destination))
            headings = {re.sub(r'[^\w\- ]', '', h).lower().replace(' ', '-')
                        for h in re.findall(r'^#+ (.+)$', destination, re.M)}
            if fragment not in explicit | headings:
                errors.append(f'{path.relative_to(root)}: missing anchor {target}')

for ident, count in Counter(ids).items():
    if count != 1:
        errors.append(f'duplicate lesson ID: {ident}')
progress = (root/'roadmap/progress.md').read_text().split('## История прежних записей')[0]
journal_ids = re.findall(r'^\| \[([A-Z]+-\d+) —', progress, re.M)
if Counter(journal_ids) != Counter(ids):
    errors.append('journal must contain each lesson exactly once')
matrix = (root/'roadmap/matrix-coverage.md').read_text()
rows = re.findall(r'^\| (TechSkills Frontend|SoftSkills) / A(\d+) \|', matrix, re.M)
if len(set(rows)) != len(rows):
    errors.append('duplicate source row')
counts = Counter(sheet for sheet, _ in rows)
if counts != {'TechSkills Frontend': 132, 'SoftSkills': 74}:
    errors.append(f'source coverage changed: {dict(counts)}; verify against workbook')
for line in matrix.splitlines():
    if line.startswith(('| TechSkills Frontend /', '| SoftSkills /')):
        refs = re.findall(r'\[([A-Z]+-\d+)\]', line)
        if not refs or any(ref not in ids for ref in refs):
            errors.append(f'source row lacks a valid lesson: {line[:90]}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(texts)} Markdown files, {len(ids)} unique lessons, '
      f'{len(rows)} source requirements; local links, anchors and journal valid.')
