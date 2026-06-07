"""Pure utility functions for generating the active daily boilerplate."""

import ast
import re
import textwrap

from pathlib import Path

from .constants import TEXT_WIDTH


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
