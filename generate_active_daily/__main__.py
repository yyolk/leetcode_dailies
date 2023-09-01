import ast
import asyncio
import textwrap
import json

from datetime import datetime
from pathlib import Path

import black

from bs4 import BeautifulSoup
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from markdownify import markdownify

TEXT_WIDTH = 82


async def main():
    transport = AIOHTTPTransport(url="https://leetcode.com/graphql/")

    async with Client(
        transport=transport, fetch_schema_from_transport=False
    ) as session:
        query = gql(
            """
            query questionOfToday {
                activeDailyCodingChallengeQuestion {
                    date
                    # userStatus
                    link
                    question {
                    #   acRate
                    difficulty
                    #   freqBar
                    frontendQuestionId: questionFrontendId
                    #   isFavor
                    paidOnly: isPaidOnly
                    #   status
                    title
                    titleSlug
                    #   hasVideoSolution
                    #   hasSolution
                    codeDefinition
                    content
                    # topicTags {
                    #   name
                    #   id
                    #   slug
                    # }
                    }
                }
            }
            """
        )

        result = await session.execute(query)
        return result


def modify_class_docstring(code, new_docstring, first_line):
    # Parse the code into an abstract syntax tree (AST)
    parsed_tree = ast.parse(code)

    # Iterate through the nodes in the parsed AST
    for node in ast.walk(parsed_tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            found_docstring = False
            for item in node.body:
                if isinstance(item, ast.Expr) and isinstance(item.value, ast.Str):
                    item.value.s = new_docstring  # Modify the docstring
                    found_docstring = True

            # If no existing docstring is found, add a new docstring
            if not found_docstring:
                docstring = ast.Expr(value=ast.Str(s=""))
                indentation = node.body[0].col_offset
                indented_docstring = (
                    first_line
                    + "\n"
                    + textwrap.indent(new_docstring, " " * indentation)
                )

                docstring.value.s = indented_docstring
                node.body.insert(0, docstring)

    # Convert the modified AST back to code
    modified_code = ast.unparse(parsed_tree)
    return modified_code

def write_file(directory_path, filename, content):
    # Create a Path object for the directory
    directory = Path(directory_path)
    
    # Create the directory if it doesn't exist
    directory.mkdir(parents=True, exist_ok=True)
    
    # Create a Path object for the file within the directory
    file_path = directory / filename
    
    # Write content to the file
    with open(file_path, 'w') as file:
        file.write(content)


results = asyncio.run(main())

html_summary = results["activeDailyCodingChallengeQuestion"]["question"]["content"]
soup = BeautifulSoup(html_summary, "html.parser")
example_starts = soup.find("strong", class_="example").parent

content_before_example = "".join(
    str(content) for content in soup.contents[: soup.contents.index(example_starts)]
)


initial_python_code = next(
    filter(
        lambda x: x["value"] == "python3",
        json.loads(
            results["activeDailyCodingChallengeQuestion"]["question"]["codeDefinition"]
        ),
    )
)["defaultCode"] + (
    " " * 8 + "..."
)  # add an elipsis into the default solution method so AST can parse, the 8th column is a guess!
challenge_question_id = results["activeDailyCodingChallengeQuestion"]["question"][
    "frontendQuestionId"
]
challenge_slug = results["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
challenge_title = results["activeDailyCodingChallengeQuestion"]["question"]["title"]
# our docstring is pretty simple, everything before the examples, the number and the title
docstring_ = markdownify(content_before_example)

lines_ = filter(lambda x: x, docstring_.splitlines())
wrapped_docstring = (
    # include a blank line in-between every lines
    "\n\n".join(
        [
            # join the wrapped lines with a new line
            "\n".join(textwrap.wrap(line, TEXT_WIDTH))
            for line in lines_
        ]
    )
)

# print(wrapped_docstring)

first_line_ = f"{challenge_question_id}. {challenge_title}\n"
modified_code = modify_class_docstring(
    initial_python_code, wrapped_docstring, first_line_
)
# print(modified_code)
# for sanity, send it through black's formatter
final_boilerplate = black.format_str(modified_code, mode=black.FileMode(line_length=TEXT_WIDTH))

current_month_answer_folder = f"{datetime.utcnow():%Y%m}"
current_active_daily_problem_file = f"{datetime.utcnow():%Y%m%d}.py"

write_file(current_month_answer_folder, current_active_daily_problem_file, final_boilerplate)
print(f"Wrote {current_month_answer_folder}/{current_active_daily_problem_file}.")
print("With content:")
print(final_boilerplate)
