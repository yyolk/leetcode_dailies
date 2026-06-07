"""Tests for generate_problem_symlinks."""

from pathlib import Path

from generate_problem_symlinks import __main__ as symlink_main
from generate_problem_symlinks.utils import extract_problem_number


class TestExtractProblemNumber:
    def test_extracts_number_from_docstring(self, tmp_path):
        solution_file = tmp_path / "20240101.py"
        solution_file.write_text('class Solution:\n    """1234. Example"""\n')
        assert extract_problem_number(solution_file) == "1234"

    def test_returns_none_when_number_missing(self, tmp_path):
        solution_file = tmp_path / "20240101.py"
        solution_file.write_text("class Solution:\n    pass\n")
        assert extract_problem_number(solution_file) is None


class TestMain:
    def test_generates_by_problem_symlink(self, tmp_path, monkeypatch):
        solutions_dir = tmp_path / "solutions"
        source_dir = solutions_dir / "2024" / "202401"
        source_dir.mkdir(parents=True)
        source_file = source_dir / "20240115.py"
        source_file.write_text('class Solution:\n    """77. Combinations"""\n')

        by_problem_dir = solutions_dir / "zz_by_problem_number"
        monkeypatch.setattr(symlink_main, "BASE_SOLUTIONS_DIR", solutions_dir)
        monkeypatch.setattr(symlink_main, "BY_PROBLEM_DIR", by_problem_dir)
        symlink_main.main()

        link = by_problem_dir / "77_20240115.py"
        assert link.is_symlink()
        assert link.readlink() == Path("../2024/202401/20240115.py")
