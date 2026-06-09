"""Pure utility functions for generating the active daily boilerplate."""

import ast
import re
import textwrap
import unicodedata

from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

from .constants import TEXT_WIDTH

_DOCSTRING_SECTION_HEADING_RE = re.compile(r"^\s*([A-Za-z][A-Za-z ]+):\s*$")
_DOCSTRING_ARG_WITH_TYPE_RE = re.compile(
    r"^(\s*)(\*{0,2}[A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\):(?:\s*(.*))?$"
)
_DOCSTRING_RET_WITH_TYPE_RE = re.compile(r"^(\s*)([^:]+):(?:\s*(.*))?$")
_COMPLEX_TYPE_INDICATORS = "[]|,.\"'()"
_SIMPLE_RETURN_TYPES = {
    "none",
    "any",
    "bool",
    "int",
    "float",
    "str",
    "bytes",
    "dict",
    "list",
    "tuple",
    "set",
    "frozenset",
    "object",
}


def extract_constraints_lines(html_content):
    """Extracts the Constraints section from a LeetCode question HTML payload."""
    soup = BeautifulSoup(html_content, "html.parser")
    constraints_heading = soup.find(
        "strong", string=lambda text: text and text.strip() == "Constraints:"
    )
    if constraints_heading is None:
        return []

    constraints_container = (
        constraints_heading.find_parent("p") or constraints_heading.parent
    )
    constraints_html = str(constraints_container)
    constraints_list = constraints_container.find_next_sibling("ul")
    if constraints_list is not None:
        constraints_html += str(constraints_list)

    constraints_docstring = unicodedata.normalize("NFKC", markdownify(constraints_html))
    constraints_lines = [line for line in constraints_docstring.splitlines() if line]
    if constraints_lines and constraints_lines[0] == "**Constraints:**":
        constraints_lines[0] = "Constraints:"
    return constraints_lines


def camel_to_snake(camel_string):
    """Converts a camelCase name into a snake_case name."""
    # Use regular expressions to find all uppercase letters
    # and add an underscore before them
    snake_string = re.sub(r"([A-Z])", r"_\1", camel_string)

    # Remove any leading underscore and convert to lowercase
    snake_string = snake_string.lstrip("_").lower()

    return snake_string


def wrap_docstring(lines, indentation=0):
    """Makes a docstring like we like it from leetcode"""
    new_docstring = (
        # include a blank line in-between every lines
        "\n\n".join(
            [
                # join the wrapped lines with a new line
                "\n".join(textwrap.wrap(line, TEXT_WIDTH - indentation))
                for line in lines
            ]
        )
    )
    return new_docstring


def remove_redundant_google_docstring_types(docstring):
    """Removes redundant type annotations from Google-style Args/Returns sections."""
    had_trailing_newline = docstring.endswith("\n")
    lines = docstring.splitlines()
    updated_lines = []
    active_section = None
    active_section_indent = 0

    for line in lines:
        stripped = line.strip()
        indentation = len(line) - len(line.lstrip(" "))

        if active_section and stripped and indentation <= active_section_indent:
            active_section = None

        heading_match = _DOCSTRING_SECTION_HEADING_RE.match(line)
        if heading_match:
            heading = heading_match.group(1).lower()
            if heading in {"args", "arguments", "returns"}:
                active_section = heading
                active_section_indent = indentation
            else:
                active_section = None
            updated_lines.append(line)
            continue

        if active_section in {"args", "arguments"}:
            arg_match = _DOCSTRING_ARG_WITH_TYPE_RE.match(line)
            if arg_match:
                arg_indent, arg_name, arg_desc = arg_match.groups()
                line = f"{arg_indent}{arg_name}:"
                if arg_desc:
                    line = f"{line} {arg_desc}"
                updated_lines.append(line)
                continue

        if active_section == "returns":
            return_match = _DOCSTRING_RET_WITH_TYPE_RE.match(line)
            if return_match:
                return_indent, return_type, return_desc = return_match.groups()
                stripped_return_type = return_type.strip()
                normalized_return_type = stripped_return_type.lower()
                looks_like_complex_type = any(
                    char in return_type for char in _COMPLEX_TYPE_INDICATORS
                )
                if (
                    normalized_return_type in _SIMPLE_RETURN_TYPES
                    or looks_like_complex_type
                    or (stripped_return_type and stripped_return_type[0].isupper())
                ) and return_desc:
                    updated_lines.append(f"{return_indent}{return_desc}")
                    continue

        updated_lines.append(line)

    result = "\n".join(updated_lines)
    if had_trailing_newline:
        result += "\n"
    return result


def _annotation_to_google_style(annotation):
    if annotation is None:
        return None
    if isinstance(annotation, ast.Name):
        return annotation.id
    if isinstance(annotation, ast.Constant):
        return str(annotation.value)
    if isinstance(annotation, ast.Attribute):
        return annotation.attr
    if isinstance(annotation, ast.Subscript):
        base = _annotation_to_google_style(annotation.value)
        if isinstance(annotation.slice, ast.Tuple):
            parts = [
                _annotation_to_google_style(item) or "value"
                for item in annotation.slice.elts
            ]
            inner = " and ".join(parts)
        else:
            inner = _annotation_to_google_style(annotation.slice) or "value"
        return f"{base} of {inner}" if base else inner
    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        left = _annotation_to_google_style(annotation.left) or "value"
        right = _annotation_to_google_style(annotation.right) or "value"
        return f"{left} or {right}"
    if isinstance(annotation, ast.Tuple):
        parts = [_annotation_to_google_style(item) or "value" for item in annotation.elts]
        return " and ".join(parts)
    try:
        return ast.unparse(annotation)
    except Exception:  # pragma: no cover
        return "value"


def _build_method_docstring(function_node):
    docstring_lines = ["...", "", "Proposed solution ..."]
    args = [arg for arg in function_node.args.args if arg.arg != "self"]
    if args:
        docstring_lines.extend(["", "Args:"])
        for arg in args:
            arg_type = _annotation_to_google_style(arg.annotation)
            if arg_type:
                docstring_lines.append(f"    {arg.arg} ({arg_type}): ...")
            else:
                docstring_lines.append(f"    {arg.arg}: ...")

    return_type = _annotation_to_google_style(function_node.returns)
    if return_type:
        docstring_lines.extend(["", "Returns:", f"    {return_type}: ..."])
    return "\n".join(docstring_lines)


def modify_class_docstring(code, new_docstring, first_line):
    """This is a rough ast parse and modify"""
    # The types we'll want to enforce to lowercase while walking the AST
    # (no requirement for attr(typing, "GenericT"))
    generic_types_pep_585 = [
        "Tuple",
        "List",
        "Dict",
        "Set",
        "FrozenSet",
        "Type",
    ]
    # Parse the code into an abstract syntax tree (AST)
    parsed_tree = ast.parse(code)

    # We'll need to know these for renaming the method name and redirecting the caller.
    # The majority of the time, leetcode expects to call a Solution.method(...).
    # This is the only case it satisfies, other cases, i.e., where it wants an interface
    # will need better detection and handled differently.
    camel_case_function_name = None
    snake_case_function_name = None
    # We'll want to keep track of the old arg names for renaming those references in
    # the problem description.
    args_list = []

    # Iterate through the nodes in the parsed AST
    for node in ast.walk(parsed_tree):
        # Work on the boilerplate method that's tied to the Solution(...)
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith("__") and node.name.endswith("__"):
                continue
            # Leetcode follows snake_case conventions elsewhere,
            # but doesn't for python for some reason.
            # Save for later
            camel_case_function_name = node.name
            snake_case_function_name = camel_to_snake(node.name)
            # Make the method name snake_case.
            node.name = snake_case_function_name
            # Work on the boilerplate Solution.method(...)'s args
            for arg in node.args.args:
                # We don't need to do anything with self.
                # In the future we might have detectable scenarios where we necessarily need to
                # switch it out to cls and add a @classmethod decorator.
                if arg.arg == "self":
                    continue
                # Save the old arg name for identifying references in our problem
                # description.
                args_list.append(arg.arg)
                # Make the args, leetcode makes camelCase, snake_case.
                # Leetcode invokes methods positionally so this superficial change is trivial.
                arg.arg = camel_to_snake(arg.arg)
                # Dumb way to enforce PEP-585 with the boilerplate code leetcode generates,
                # but since we are already here, might as well do it.
                # This section works on the function args.
                if isinstance(arg.annotation, ast.Subscript):
                    for arg_node in ast.walk(arg.annotation):
                        # Reassign the arg_node.id with a Call on lower() on the use
                        # of the types in the predicate (matched by string).
                        if (
                            isinstance(arg_node, ast.Name)
                            and isinstance(arg_node.id, str)
                            and arg_node.id in generic_types_pep_585
                        ):
                            arg_node.id = arg_node.id.lower()
            # Dumb way to enforce PEP-585 with the boilerplate code leetcode generates,
            # but since we are already here we might as well do it.
            # This section works on the function return type annotation.
            if node.returns is not None:
                for r_arg in ast.walk(node.returns):
                    if isinstance(r_arg, ast.Subscript):
                        for r_arg_node in ast.walk(r_arg):
                            if (
                                isinstance(r_arg_node, ast.Name)
                                and isinstance(r_arg_node.id, str)
                                and r_arg_node.id in generic_types_pep_585
                            ):
                                r_arg_node.id = r_arg_node.id.lower()

            if (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            ):
                node.body[0].value.value = remove_redundant_google_docstring_types(
                    node.body[0].value.value
                )
            else:
                node.body.insert(
                    0, ast.Expr(value=ast.Constant(value=_build_method_docstring(node)))
                )

    # We go back in after walking the entire thing so we can append into the class
    # Probably could make this one loop but can revisit since the above needs refactoring too
    for node in ast.walk(parsed_tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            found_docstring = False
            for item in node.body:
                if isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant):
                    # Modify the docstring...
                    # we're using just the raw lines in place here if its already found
                    item.value.value = new_docstring
                    found_docstring = True

            # If no existing docstring is found, add a new docstring
            # There should always be no docstring found for the most used case
            if not found_docstring:
                # Find all the references to our new args which were camelCase,
                # make them snake_case.
                for arg in args_list:
                    # This is a naive approach, it is the full text.
                    # A better approach may be required in the future.
                    # A low-effort addition could be using regex to detect
                    # those references as markdown code-spans.
                    # e.g., "`namedVar[x + y]`"
                    new_docstring = [
                        line.replace(arg, camel_to_snake(arg)) for line in new_docstring
                    ]

                # Set up a docstring, and reference our indentation for the class
                # Solution(...).
                docstring = ast.Expr(value=ast.Constant(value=""))
                indentation = node.body[0].col_offset
                # Rewrite new_docstring, wrapping it.
                # We know our indentation for keeping TEXT_WIDTH aligned.
                new_docstring = wrap_docstring(new_docstring, indentation)
                indented_docstring = (
                    first_line
                    + "\n"
                    + textwrap.indent(new_docstring, " " * indentation)
                )

                docstring.value.value = indented_docstring
                node.body.insert(0, docstring)

            # Create a new function assignment to assign the camelCase function to our
            # snake_case, we want leetcode to call our snake_case function.
            if (
                camel_case_function_name
                and snake_case_function_name
                and camel_case_function_name != snake_case_function_name
            ):
                new_attribute = ast.Assign(
                    # Set a valid lineno, 0 seems to work fine
                    lineno=0,
                    # Set a valid col_offset, 0 seems to work fine
                    col_offset=0,
                    targets=[ast.Name(id=camel_case_function_name, ctx=ast.Store())],
                    value=ast.Name(id=snake_case_function_name, ctx=ast.Load()),
                )
                # Append the new attribute, which is our function redirection to the class
                # Solution(...) body
                node.body.append(new_attribute)

    # Convert the modified AST back to code
    return ast.unparse(parsed_tree)


def write_file(directory_path, filename, content, overwrite=False):
    """Holds the file creation logic"""
    # Create a Path object for the directory
    directory: Path = Path(directory_path)

    # Create the directory if it doesn't exist
    directory.mkdir(parents=True, exist_ok=True)

    # Create a Path object for the file within the directory
    file_path: Path = directory / filename

    # Check if file exists
    if file_path.exists() and not overwrite:
        raise FileExistsError

    # Write content to the file
    with open(file_path, "w") as file:
        file.write(content)
