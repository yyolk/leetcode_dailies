"""
When run, will insert the permalink to the leetcode challenge to the
top of the file as a single line comment.

This is the only file currently using most of the extra functions in 
`generate_active_daily.client(...)`
"""
import asyncio
import os
import re

from datetime import datetime


from generate_active_daily.client import (
    make_leetcode_url_from_slug,
    previous_questions,
    query_qd_challenge_question,
    query_question_of_today,
)


DIR_PATTERN = re.compile(r"\d{6}")
FILE_PATTERN = re.compile(r"\d{8}")
TARGET_DATE = datetime(year=2023, month=8, day=23)


async def main():
    todays_question = (await query_question_of_today())[
        "activeDailyCodingChallengeQuestion"
    ]
    todays_datetime = datetime.strptime(todays_question["date"], "%Y-%m-%d")

    limit = (todays_datetime - TARGET_DATE).days
    new_results = []
    async for res in previous_questions(limit):
        # all_results.append(res)
        this_q = {**res, **await query_qd_challenge_question(res["titleSlug"])}
        new_results.append(this_q)

    datetime_results = {
        datetime.strptime(result["date"], "%Y-%m-%d"): result for result in new_results
    }

    matched_directories = []
    # root, dirs, files
    for _, dirs, _ in os.walk("."):
        for dir_ in dirs:
            if DIR_PATTERN.match(dir_):
                matched_directories.append(dir_)

    for dir_ in matched_directories:
        # root, dirs, files
        for sub_root, _, sub_files in os.walk(dir_):
            for sub_file in sub_files:
                if FILE_PATTERN.match(sub_file):
                    sub_file_basename, _ = os.path.splitext(sub_file)
                    this_files_date = datetime.strptime(sub_file_basename, "%Y%m%d")
                    if this_files_date in datetime_results:
                        challenge_link = make_leetcode_url_from_slug(
                            datetime_results[this_files_date]["titleSlug"]
                        )

                        print(f"{this_files_date:%Y%m%d}.py:", challenge_link)

                        sub_file_path = f"{sub_root}/{sub_file}"
                        with open(sub_file_path, "r+") as fp:
                            content_lines = fp.readlines()
                            file_meta_challenge_link = f"# {challenge_link}"
                            first_line = content_lines[0].strip()
                            starts_with_class = first_line.startswith("class")
                            # starts_with_comment = first_line.startswith("#")
                            # starts_with_docstring = first_line.startswith('"""')
                            if not first_line == file_meta_challenge_link:
                                new_content = (
                                    file_meta_challenge_link
                                    + (("\n" * 3) if starts_with_class else "\n")
                                    + "".join(content_lines)
                                )
                                fp.seek(0)  # Rewind the tape
                                # Really write the file
                                fp.write(new_content)
                                
                                # For testing
                                # print("would've written")
                                # print(
                                #     "\n".join(new_content.splitlines()[:4]) + "....",
                                # )


if __name__ == "__main__":
    asyncio.run(main())
