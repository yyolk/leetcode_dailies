"""Tests for generate_problem_symlinks."""

from pathlib import Path

from generate_problem_symlinks import __main__ as symlink_main
from generate_problem_symlinks.utils import clear_symlink_dir, extract_problem_number, iter_solution_files


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

    def test_skips_files_without_problem_number(self, tmp_path, monkeypatch, capsys):
        solutions_dir = tmp_path / "solutions"
        source_dir = solutions_dir / "2024" / "202401"
        source_dir.mkdir(parents=True)
        (source_dir / "20240115.py").write_text('class Solution:\n    """77. Combinations"""\n')
        (source_dir / "20240116.py").write_text("class Solution:\n    pass\n")

        by_problem_dir = solutions_dir / "zz_by_problem_number"
        monkeypatch.setattr(symlink_main, "BASE_SOLUTIONS_DIR", solutions_dir)
        monkeypatch.setattr(symlink_main, "BY_PROBLEM_DIR", by_problem_dir)

        symlink_main.main()

        out = capsys.readouterr().out
        assert (by_problem_dir / "77_20240115.py").is_symlink()
        assert len(list(by_problem_dir.iterdir())) == 1
        assert "Skipping" in out
        assert "Generated 1 symlinks" in out
        assert "Skipped 1 files without problem number metadata" in out


class TestUtils:
    def test_iter_solution_files_filters_expected_layout(self, tmp_path):
        base_dir = tmp_path / "solutions"
        valid_dir = base_dir / "2024" / "202401"
        valid_dir.mkdir(parents=True)
        valid_file = valid_dir / "20240115.py"
        valid_file.write_text("pass\n")

        (base_dir / "notes").mkdir()
        (base_dir / "notes" / "20240115.py").write_text("pass\n")
        (base_dir / "2024" / "misc").mkdir(parents=True)
        (base_dir / "2024" / "misc" / "20240116.py").write_text("pass\n")

        assert list(iter_solution_files(base_dir)) == [valid_file]

    def test_clear_symlink_dir_removes_files_and_symlinks(self, tmp_path):
        by_problem_dir = tmp_path / "zz_by_problem_number"
        by_problem_dir.mkdir()
        stale_file = by_problem_dir / "stale.txt"
        stale_file.write_text("stale")

        target = tmp_path / "target.py"
        target.write_text("pass\n")
        stale_link = by_problem_dir / "stale.py"
        stale_link.symlink_to(target)

        clear_symlink_dir(by_problem_dir)

        assert not stale_file.exists()
        assert not stale_link.exists()
