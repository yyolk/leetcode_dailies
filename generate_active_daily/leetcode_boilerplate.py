import json
import re


def _split_external_block_from_solution(starter_code):
    """Splits python starter code into an external block and Solution class block."""
    solution_match = re.search(r"(?m)^class Solution\b", starter_code)
    if not solution_match:
        return "", starter_code.strip()
    return (
        starter_code[: solution_match.start()].strip(),
        starter_code[solution_match.start() :].strip(),
    )


def _strip_wrapping_python_docstring(block):
    """Strips wrapping triple-quote docstrings from starter-code metadata blocks."""
    stripped = block.strip()
    for quote in ('"""', "'''"):
        if stripped.startswith(quote) and stripped.endswith(quote):
            return stripped[len(quote) : -len(quote)].strip()
    return stripped


def _normalize_external_block_lines(external_block):
    """Converts external python starter metadata into markdown-friendly lines."""
    if not external_block:
        return []
    normalized_block = _strip_wrapping_python_docstring(external_block)
    lines = []
    for line in normalized_block.splitlines():
        if not line.strip():
            continue
        stripped = line.lstrip()
        if stripped.startswith("#"):
            stripped = stripped.lstrip("#").strip()
            if not stripped:
                continue
            lines.append(stripped)
            continue
        lines.append(line.rstrip())
    return lines


def select_python3_starter_code(question):
    """Selects the python3 starter code from codeSnippets with codeDefinition fallback."""
    code_snippets = question.get("codeSnippets") or []
    for code_snippet in code_snippets:
        if code_snippet.get("langSlug") == "python3":
            return code_snippet["code"]

    code_definition = json.loads(question["codeDefinition"])
    return next(
        filter(
            lambda language_data: language_data["value"] == "python3",
            code_definition,
        )
    )["defaultCode"]


def extract_external_docstring_lines(starter_code):
    """Builds markdown docstring lines for external classes included in starter code."""
    external_block, _ = _split_external_block_from_solution(starter_code)
    external_lines = _normalize_external_block_lines(external_block)
    if not external_lines:
        return []

    heading_line = external_lines[0]
    code_lines = external_lines[1:]
    if not code_lines:
        return []
    return [heading_line, *(f"    {line}" for line in code_lines)]


def strip_external_block_from_starter_code(starter_code):
    """Drops external starter-code metadata and keeps only the Solution template."""
    _, solution_block = _split_external_block_from_solution(starter_code)
    return solution_block
