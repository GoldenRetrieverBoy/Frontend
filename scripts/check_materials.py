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
    for lesson in re.split(r'(?=^## )', body, flags=re.M):
        heading = re.match(r'^## ([A-Z]+-\d+)\.', lesson)
        if heading and not re.search(r'<details>\s*<summary>.+?</summary>\s*\S.*?</details>', lesson, re.S):
            errors.append(f'{path.relative_to(root)}: missing practice review for {heading[1]}')
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

# The matrix owns grade membership; roadmap order is pedagogical and may change.
routes = sorted((root / 'roadmap/grades').glob('[0-9][0-9]-*.md'))
requirements = {}
for line in matrix.splitlines():
    match = re.match(r'^\| (TechSkills Frontend|SoftSkills) / A(\d+) \| ([^|]+) \|', line)
    if match:
        sheet, row, grade = match.groups()
        bucket = requirements.setdefault(grade.strip(), {'tech': set(), 'soft': set()})
        refs = re.findall(r'\[([A-Z]+-\d+)\]', line)
        if sheet == 'TechSkills Frontend':
            bucket['tech'].update((ref, row) for ref in refs)
        else:
            bucket['soft'].update(refs)

seen_grades = set()
previous_lessons = set()
for path in routes:
    route = texts[path.resolve()]
    title = re.search(r'^# Roadmap: (.+)$', route, re.M)
    grade = title[1] if title else ''
    label = str(path.relative_to(root))
    if grade not in requirements or grade in seen_grades:
        errors.append(f'{label}: unknown or duplicate grade: {grade}')
        continue
    seen_grades.add(grade)
    tech = []
    lesson_ids = []
    technical_section = re.search(r'## Технические вопросы\n(.*?)(?=\n## |\Z)', route, re.S)
    for line in (technical_section[1] if technical_section else '').splitlines():
        match = re.match(r'^\d+\. \[([A-Z]+-\d+) —', line)
        if not match:
            if re.match(r'^\s*[-*+] \[([A-Z]+-\d+)', line):
                errors.append(f'{label}: technical lesson must be numbered: {line}')
            continue
        ident = match[1]
        lesson_ids.append(ident)
        source = re.search(r'строки Excel: ([\d, ]+)\.$', line)
        if source is None:
            errors.append(f'{label}: missing source rows for {ident}')
        else:
            tech.extend((ident, row.strip()) for row in source[1].split(','))
        expected_depth = 'углубление' if ident in previous_lessons else 'впервые в маршруте'
        if f'— {expected_depth};' not in line:
            errors.append(f'{label}: wrong depth label for {ident}: expected {expected_depth}')
    if len(lesson_ids) != len(set(lesson_ids)):
        errors.append(f'{label}: duplicate technical lesson')
    soft = re.findall(r'^- \[(SOFT-\d+) —', route, re.M)
    for kind, actual in [('tech', tech), ('soft', soft)]:
        expected = requirements[grade][kind]
        missing = expected - set(actual)
        extra = set(actual) - expected
        if missing or extra or len(actual) != len(set(actual)):
            errors.append(f'{label}: {kind} grade coverage mismatch; '
                          f'missing={sorted(missing)}, extra={sorted(extra)}, '
                          f'duplicates={len(actual) - len(set(actual))}')
    previous_lessons.update(lesson_ids)
for grade in sorted(requirements.keys() - seen_grades):
    errors.append(f'missing roadmap for grade: {grade}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(texts)} Markdown files, {len(ids)} unique lessons, '
      f'{len(rows)} source requirements; local links, anchors, journal and grade coverage valid.')
