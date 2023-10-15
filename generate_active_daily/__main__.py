"""
Generates the current daily active challenge boilerplate file.

This will use the 'undocumented' graphQL endpoint for leetcode. 
We could also authenticate but we don't need the extra context it would provide.

TODO:
    - handle other boilerplate scaffolds that don't look like:
        
        class Solution:
            def myProblemSolution(self, in_: List[str]) -> int:

"""
import argparse
import ast
import asyncio
import textwrap
import json
import re
import sys
import unicodedata

from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import black

from bs4 import BeautifulSoup
from markdownify import markdownify

from .constants import LEETCODE_BASE_URL
from .client import query_question_of_today

TEXT_WIDTH = 88  # The default that psf/black ships with is 88

parser = argparse.ArgumentParser(
    description="Generates the current daily active challenge boilerplate file."
)
parser.add_argument("--url", action="store_true")
parser.add_argument("-O", "--overwrite", action="store_true", default=False)

args = parser.parse_args()


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
    # Parse the code into an abstract syntax tree (AST)
    parsed_tree = ast.parse(code)

    # We'll need to know these for renaming the method name and redirecting the caller.
    camel_case_function_name = None
    snake_case_function_name = None

    # Iterate through the nodes in the parsed AST
    for node in ast.walk(parsed_tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            found_docstring = False
            for item in node.body:
                if isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant):
                    # Modify the docstring...
                    # we're using just the raw lines in place here if its already found
                    item.value.s = new_docstring
                    found_docstring = True

            # If no existing docstring is found, add a new docstring
            # There should always be no docstring found for the most used case
            if not found_docstring:
                docstring = ast.Expr(value=ast.Constant(s=""))
                indentation = node.body[0].col_offset
                # Rewrite new_docstring, wrapping it.
                # We know our indentation for keeping TEXT_WIDTH aligned.
                new_docstring = wrap_docstring(new_docstring, indentation)
                indented_docstring = (
                    first_line
                    + "\n"
                    + textwrap.indent(new_docstring, " " * indentation)
                )

                docstring.value.s = indented_docstring
                node.body.insert(0, docstring)
        #
        # From here on, our code for modifying the AST is much better
        # The above could be refactored and the second loop below is for keeping it clean.
        #
        # Work on the boilerplate method that's tied to the Solution(...)
        if isinstance(node, ast.FunctionDef):
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
                # Make the args, leetcode makes camelCase, snake_case.
                # Leetcode invokes methods positionally so this superficial change is trivial.
                arg.arg = camel_to_snake(arg.arg)

    # We go back in after walking the entire thing so we can append into the class
    # Probably could make this one loop but can revisit since the above needs refactoring too
    for node in ast.walk(parsed_tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            # Create a new function assignment statement
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


results = asyncio.run(query_question_of_today())


challenge_url = urljoin(
    LEETCODE_BASE_URL, results["activeDailyCodingChallengeQuestion"]["link"]
)
if args.url:
    # Not the cleanest way to do it, but will refactor
    # TODO: reflow
    print(challenge_url)
    sys.exit(0)

challenge_question_id = results["activeDailyCodingChallengeQuestion"]["question"][
    "frontendQuestionId"
]
challenge_slug = results["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
challenge_title = results["activeDailyCodingChallengeQuestion"]["question"]["title"]
challenge_datetime = datetime.strptime(
    results["activeDailyCodingChallengeQuestion"]["date"], "%Y-%m-%d"
)

# Extract our problem summary from html
html_summary = results["activeDailyCodingChallengeQuestion"]["question"]["content"]
soup = BeautifulSoup(html_summary, "html.parser")
example_starts = soup.find("strong", class_="example").parent

CONTENT_BEFORE_EXAMPLE = "".join(
    str(content) for content in soup.contents[: soup.contents.index(example_starts)]
)


initial_python_code = next(
    # this is a JSONString returned from the gql endpoint, we can't filter it there
    # so filter it here, grabbing only the python3 starter code provided in the editor
    # this is what we use to add our description docstring to
    # it's also concrete in that we shouldn't change what leetcode calls to test your
    # solution - which is annoying because for python
    # since they always use camelCase instead of snake_case, blegh
    filter(
        lambda x: x["value"] == "python3",
        json.loads(
            results["activeDailyCodingChallengeQuestion"]["question"]["codeDefinition"]
        ),
    )
)["defaultCode"] + (
    # add an elipsis into the default solution method so AST can parse, the 8th column is a guess!
    # TODO: upon encountering a challenge like 20208/20230828.py, this will have to be refactored
    " " * 8
    + "..."
)

# our docstring is pretty simple, everything before the examples, the number and the title
# see #4, potentially an edge case, normalize \xa0 (&nbsp;) to ' ' using NFKC
# NFKC = normal form compatibility decomposition followed by canonical composition
docstring_ = unicodedata.normalize("NFKC", markdownify(CONTENT_BEFORE_EXAMPLE))

lines_ = filter(lambda x: x, docstring_.splitlines())
# We're being explicit in our definition and setting it twice...
# Our `lines_` come from the `unicode.normalize(...)`,
# which is also our `unwrapped_docstring`
unwrapped_docstring = lines_

# The first line in the docstring is always: '#No. Title of Challenge'
first_line_ = f"{challenge_question_id}. {challenge_title}\n"
# The complete modified code includes the modified docstring
MODIFIED_CODE = modify_class_docstring(
    initial_python_code, unwrapped_docstring, first_line_
)
# We insert '# https://leetcode.com/....' at the top of the file
boilerplate = f"# {challenge_url}" + "\n" * 3 + MODIFIED_CODE

# For extra sanity, send it through black's formatter,
# this ends up catching a lot of small things,
# like the last-line triple-quotes being indented from ast.unparse(...)
final_boilerplate = black.format_str(
    boilerplate, mode=black.FileMode(line_length=TEXT_WIDTH)
)

now = datetime.utcnow()
current_month_answer_folder = f"{now:%Y%m}"
current_active_daily_problem_file = f"{now:%Y%m%d}.py"

# Sanity check, see if our date matches
if datetime(year=now.year, month=now.month, day=now.day) != challenge_datetime:
    raise ValueError("The daily problem doesn't match our clock's UTC time.")

try:
    write_file(
        current_month_answer_folder,
        current_active_daily_problem_file,
        final_boilerplate,
        args.overwrite,
    )
    print(f"Wrote {current_month_answer_folder}/{current_active_daily_problem_file}.")
    print("With content:")
except FileExistsError:
    print("File already exists! Skipping.")
    print("Content would have been:")
finally:
    print()
    print(final_boilerplate)
