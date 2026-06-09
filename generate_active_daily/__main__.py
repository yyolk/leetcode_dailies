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
import asyncio
import sys
import unicodedata

from datetime import datetime
from urllib.parse import urljoin

import black

from bs4 import BeautifulSoup
from markdownify import markdownify

from .constants import LEETCODE_BASE_URL, TEXT_WIDTH
from .client import query_question_of_today
from .leetcode_boilerplate import (
    extract_definition_footnote_lines,
    extract_external_docstring_lines,
    select_python3_starter_code,
    strip_external_block_from_starter_code,
)
from .utils import modify_class_docstring, write_file

parser = argparse.ArgumentParser(
    description="Generates the current daily active challenge boilerplate file."
)
parser.add_argument("--url", action="store_true")
parser.add_argument("-O", "--overwrite", action="store_true", default=False)

args = parser.parse_args()


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
example_starts = soup.find("p", string="\xa0")

CONTENT_BEFORE_EXAMPLE = (
    "".join(
        str(content) for content in soup.contents[: soup.contents.index(example_starts)]
    )
    # See #31, since we're splitting at `\xa0` (`&nbsp;`) we'll add it here to ensure
    # docstrings end the way we want them to be stylized.
    + "<p>&nbsp;</p>"
)


question_data = results["activeDailyCodingChallengeQuestion"]["question"]
python3_starter_code = select_python3_starter_code(question_data)
external_docstring_lines = extract_external_docstring_lines(python3_starter_code)
definition_footnote_lines = extract_definition_footnote_lines(html_summary)
initial_python_code = strip_external_block_from_starter_code(python3_starter_code) + (
    # add an elipsis into the default solution method so AST can parse, the 8th column is a guess!
    # TODO: upon encountering a challenge like 20208/20230828.py, this will have to be refactored
    " " * 8 + "..."
)

# our docstring is pretty simple, everything before the examples, the number and the title
# see #4, potentially an edge case, normalize \xa0 (&nbsp;) to ' ' using NFKC
# NFKC = normal form compatibility decomposition followed by canonical composition
docstring_ = unicodedata.normalize("NFKC", markdownify(CONTENT_BEFORE_EXAMPLE))

lines_ = filter(lambda x: x, docstring_.splitlines())
# We're being explicit in our definition and setting it twice...
# Our `lines_` come from the `unicode.normalize(...)`,
# which is also our `unwrapped_docstring`
# We also end up using this more than once over all items so list(...) here.
unwrapped_docstring = list(lines_)

if definition_footnote_lines:
    unwrapped_docstring.extend(definition_footnote_lines)

if external_docstring_lines:
    existing_docstring_lines = [
        line.strip() for line in unwrapped_docstring if line.strip()
    ]
    candidate_external_lines = [
        line.strip() for line in external_docstring_lines if line.strip()
    ]
    existing_docstring_content = "\n" + "\n".join(existing_docstring_lines) + "\n"
    candidate_external_content = "\n" + "\n".join(candidate_external_lines) + "\n"
    has_external_block = candidate_external_content in existing_docstring_content
    if not has_external_block:
        unwrapped_docstring.extend(external_docstring_lines)

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
current_month_answer_folder = f"solutions/{now:%Y}/{now:%Y%m}"
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
