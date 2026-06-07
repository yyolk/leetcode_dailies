"""Backfills solution files by removing redundant Google-style docstring type annotations."""

import argparse

from pathlib import Path

from .utils import remove_redundant_google_docstring_types


def iter_solution_files(root):
    """Yields all Python solution files under the provided root."""
    for file_path in sorted(root.rglob("*.py")):
        if "__pycache__" not in file_path.parts:
            yield file_path


def main():
    parser = argparse.ArgumentParser(
        description="Backfill solution docstrings by removing redundant Args/Returns types."
    )
    parser.add_argument(
        "--solutions-root",
        default="solutions",
        help="Directory containing solution files (default: solutions).",
    )
    args = parser.parse_args()

    solutions_root = Path(args.solutions_root)
    updated_files = 0

    for solution_file in iter_solution_files(solutions_root):
        original_content = solution_file.read_text()
        updated_content = remove_redundant_google_docstring_types(original_content)
        if updated_content != original_content:
            solution_file.write_text(updated_content)
            updated_files += 1

    print(f"Updated {updated_files} files.")


if __name__ == "__main__":
    main()
