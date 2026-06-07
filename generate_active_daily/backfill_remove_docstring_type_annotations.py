"""Backfills solution files by removing redundant Google-style docstring type annotations."""

import argparse
import ast

from pathlib import Path

from .utils import remove_redundant_google_docstring_types


def iter_solution_files(root):
    """Yields all Python solution files under the provided root."""
    for file_path in sorted(root.rglob("*.py")):
        if "__pycache__" not in file_path.parts:
            yield file_path


def _line_offsets(content):
    offsets = [0]
    running = 0
    for line in content.splitlines(keepends=True):
        running += len(line)
        offsets.append(running)
    return offsets


def _to_offset(line_offsets, lineno, col_offset):
    return line_offsets[lineno - 1] + col_offset


def _iter_docstring_nodes(parsed_tree):
    node_types = (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
    for node in ast.walk(parsed_tree):
        if not isinstance(node, node_types) or not node.body:
            continue
        first_stmt = node.body[0]
        if (
            isinstance(first_stmt, ast.Expr)
            and isinstance(first_stmt.value, ast.Constant)
            and isinstance(first_stmt.value.value, str)
        ):
            yield first_stmt.value


def _as_triple_quoted(value):
    # Escape backslashes and embedded triple quotes before wrapping.
    escaped = value.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return f'"""{escaped}"""'


def update_docstrings_in_source(content):
    """Updates redundant types in docstrings and returns updated source content."""
    parsed_tree = ast.parse(content)
    line_offsets = _line_offsets(content)
    replacements = []

    for docstring_node in _iter_docstring_nodes(parsed_tree):
        updated_docstring = remove_redundant_google_docstring_types(
            docstring_node.value
        )
        if updated_docstring == docstring_node.value:
            continue
        if not all(
            hasattr(docstring_node, field)
            for field in ("lineno", "col_offset", "end_lineno", "end_col_offset")
        ):
            continue
        start = _to_offset(
            line_offsets, docstring_node.lineno, docstring_node.col_offset
        )
        end = _to_offset(
            line_offsets, docstring_node.end_lineno, docstring_node.end_col_offset
        )
        replacements.append((start, end, _as_triple_quoted(updated_docstring)))

    if not replacements:
        return content

    updated_content = content
    for start, end, replacement in sorted(replacements, reverse=True):
        updated_content = updated_content[:start] + replacement + updated_content[end:]

    return updated_content


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
        updated_content = update_docstrings_in_source(original_content)
        if updated_content != original_content:
            solution_file.write_text(updated_content)
            updated_files += 1

    print(f"Updated {updated_files} files.")


if __name__ == "__main__":
    main()
