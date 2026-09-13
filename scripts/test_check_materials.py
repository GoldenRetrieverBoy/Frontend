"""Exercise the checker against edited, isolated copies of the real materials."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
INTERN = 'roadmap/grades/00-intern-base.md'


class MaterialChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for source in [*ROOT.rglob('*.md'), ROOT / 'scripts/check_materials.py']:
            if '.git' in source.parts:
                continue
            target = self.root / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def edit(self, name, transform):
        path = self.root / name
        original = path.read_text(encoding='utf-8')
        changed = transform(original)
        self.assertNotEqual(original, changed, 'test mutation must change its fixture')
        path.write_text(changed, encoding='utf-8')

    def check(self, expected_error=None):
        result = subprocess.run(
            [sys.executable, str(self.root / 'scripts/check_materials.py')],
            capture_output=True, text=True, timeout=10,
        )
        if expected_error is None:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn(expected_error, result.stdout)

    def test_current_materials(self):
        self.check()

    def test_missing_technical_lesson(self):
        self.edit(INTERN, lambda text: re.sub(r'^\d+\. \[JS-18[^\n]+\n', '', text, flags=re.M))
        self.check('tech grade coverage mismatch')

    def test_wrong_source_row(self):
        self.edit(INTERN, lambda text: text.replace('строки Excel: 3.', 'строки Excel: 4.'))
        self.check('tech grade coverage mismatch')

    def test_requirement_moved_to_wrong_grade(self):
        self.edit('roadmap/matrix-coverage.md', lambda text: text.replace(
            '| TechSkills Frontend / A3 | Intern: база перед Junior |',
            '| TechSkills Frontend / A3 | Junior 1 |',
        ))
        self.check('tech grade coverage mismatch')

    def test_duplicate_technical_lesson(self):
        def duplicate(text):
            line = re.search(r'^\d+\. \[JS-18[^\n]+', text, re.M)[0]
            return text.replace(line, line + '\n' + line)
        self.edit(INTERN, duplicate)
        self.check('duplicate technical lesson')

    def test_missing_soft_skill(self):
        self.edit(INTERN, lambda text: re.sub(r'^- \[SOFT-003[^\n]+\n', '', text, flags=re.M))
        self.check('soft grade coverage mismatch')

    def test_wrong_depth(self):
        self.edit(INTERN, lambda text: text.replace('впервые в маршруте', 'углубление', 1))
        self.check('wrong depth label')

    def test_grade_missing_even_without_broken_links(self):
        path = self.root / 'roadmap/grades/07-senior.md'
        path.rename(path.with_name('senior.md'))
        for source in self.root.rglob('*.md'):
            text = source.read_text(encoding='utf-8')
            source.write_text(text.replace('07-senior.md', 'senior.md'), encoding='utf-8')
        self.check('missing roadmap for grade: Senior (top)')

    def test_reordering_lessons_is_allowed(self):
        def reorder(text):
            lines = text.splitlines()
            positions = [i for i, line in enumerate(lines) if re.match(r'^\d+\. ', line)]
            entries = [re.sub(r'^\d+\. ', '', lines[i]) for i in positions][::-1]
            for number, (position, entry) in enumerate(zip(positions, entries), 1):
                lines[position] = f'{number}. {entry}'
            return '\n'.join(lines) + '\n'
        self.edit(INTERN, reorder)
        self.check()

    def test_missing_hidden_review(self):
        self.edit('fundamentals/typescript.md', lambda text: re.sub(
            r'<details>.*?</details>', '', text, count=1, flags=re.S,
        ))
        self.check('missing practice review for TS-01')

    def test_unnumbered_technical_lesson(self):
        self.edit(INTERN, lambda text: re.sub(r'^\d+\. (?=\[JS-18)', '- ', text, flags=re.M))
        self.check('technical lesson must be numbered')


if __name__ == '__main__':
    unittest.main()
