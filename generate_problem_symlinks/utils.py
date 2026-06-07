"""Utilities for generating problem-number symlinks."""

import re

from pathlib import Path

BASE_SOLUTIONS_DIR = Path("solutions")
BY_PROBLEM_DIR = BASE_SOLUTIONS_DIR / "zz_by_problem_number"
YEAR_DIR_PATTERN = re.compile(r"^\d{4}$")
MONTH_DIR_PATTERN = re.compile(r"^\d{6}$")
SOLUTION_FILE_PATTERN = re.compile(r"^\d{8}\.[^.]+$")
PROBLEM_NUMBER_PATTERN = re.compile(r'^\s*(?:[rRuUfFbB]{0,2}["\']{3}|#)\s*(\d+)\.', re.M)
# Matches `"""123.` (optionally prefixed like r"""...`) or `# 123.` lines.


def extract_problem_number(solution_file: Path) -> str | None:
    """Extract frontend problem number from a solution file."""
    content = solution_file.read_text()
    match = PROBLEM_NUMBER_PATTERN.search(content)
    if match is None:
        return None
    return match.group(1)


def iter_solution_files(base_solutions_dir: Path):
    """Iterate known solution files from year/month directories."""
    for year_dir in sorted(base_solutions_dir.iterdir()):
        if not year_dir.is_dir() or not YEAR_DIR_PATTERN.match(year_dir.name):
            continue
        for month_dir in sorted(year_dir.iterdir()):
            if not month_dir.is_dir() or not MONTH_DIR_PATTERN.match(month_dir.name):
                continue
            for file_path in sorted(month_dir.iterdir()):
                if file_path.is_file() and SOLUTION_FILE_PATTERN.match(file_path.name):
                    yield file_path


def clear_symlink_dir(by_problem_dir: Path):
    """Clear existing generated symlinks directory."""
    if not by_problem_dir.exists():
        return
    for child in by_problem_dir.iterdir():
        if child.is_symlink() or child.is_file():
            child.unlink()
