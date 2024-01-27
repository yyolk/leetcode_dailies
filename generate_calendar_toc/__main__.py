"""
Generate a table of contents per solution directory.

The TOC in this case is a calendar with hyperlinked days.

This also serves as a way to track which days weren't completed,
as it will not link to a file that doesn't exist for the given day.
"""

import calendar
import os
import re

from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup


SOLUTIONS_DIR_PATTERN = re.compile(r"\d{6}")
FILE_PATTERN = re.compile(r"\d{8}")
DAYS_PATTERN = re.compile(r"\d")

matching_directories = []
matching_files = {}

# Loop at the base of the repository for matching solution directories
for root, dirs, files in os.walk("."):
    for dir_name in dirs:
        if SOLUTIONS_DIR_PATTERN.match(dir_name):
            matching_directories.append(Path(os.path.join(root, dir_name)))

# Loop over our directories to get the files within
for dir_ in matching_directories:
    for root, dirs, files in os.walk(dir_):
        for file_name in files:
            # Does this file_name match our FILE_PATTERN
            if FILE_PATTERN.match(file_name):
                # Our file is at dir/file_name
                file_ = dir_ / file_name
                # Extract the date from the filename
                extracted_date = datetime.strptime(file_.stem, "%Y%m%d")
                # Set the Path(file) to it's datetime index, for easy lookup
                matching_files[extracted_date] = file_

# Loop again, just to keep it straight forward
for dir_ in matching_directories:
    readme = Path(dir_ / "README.md")
    # Create a calendar with a Sunday starting day
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    # Extract the date as a datetime
    dir_date = datetime.strptime(str(dir_), "%Y%m")
    # Create a soup for modifying the calendar easily
    soup = BeautifulSoup(cal.formatmonth(dir_date.year, dir_date.month), "html.parser")
    # HTMLCalendar has every day as a <td />
    for el in soup.find_all("td", string=DAYS_PATTERN):
        # Extract the day from the <td>
        day = int(el.get_text())
        # Our lookup index is our current position in the calendar
        idx = dir_date.replace(day=day)
        # Does this day have a file to match?
        if idx in matching_files:
            path_ = matching_files[idx]
            el.string.wrap(soup.new_tag("a", href=str(path_.name)))
    # Set the align attribute to center, which works on markdown rendering for the <table />
    soup.table["align"] = "center"
    # The only content in the file will be the output of the HTMLCalendar
    readme_content = soup.prettify()
    # 'Log' that we're writing our readme
    print(f"Writing {readme}")
    # Write the file
    readme.write_text(readme_content)
