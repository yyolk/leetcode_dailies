"""Generate calendar TOCs for month dirs, year dirs, and the root README."""

import calendar

from collections import defaultdict
from datetime import datetime

from bs4 import BeautifulSoup

from .utils import (
    BASE_SOLUTIONS_DIR,
    FILE_PATTERN,
    MONTH_DIR_PATTERN,
    build_year_calendar_html,
    replace_or_append_root_calendar_section,
    wrap_solved_days_with_links,
)


month_directories = []
solved_files_by_date = {}
solved_months_by_year = defaultdict(set)

for month_dir in BASE_SOLUTIONS_DIR.glob("*/*"):
    if not month_dir.is_dir() or not MONTH_DIR_PATTERN.match(month_dir.name):
        continue

    month_directories.append(month_dir)

    for file_path in month_dir.glob("*.py"):
        if FILE_PATTERN.match(file_path.name):
            extracted_date = datetime.strptime(file_path.stem, "%Y%m%d")
            solved_files_by_date[extracted_date] = file_path
            solved_months_by_year[extracted_date.year].add(extracted_date.month)

for month_dir in sorted(month_directories):
    readme = month_dir / "README.md"
    dir_date = datetime.strptime(month_dir.name, "%Y%m")
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    month_soup = BeautifulSoup(
        cal.formatmonth(dir_date.year, dir_date.month), "html.parser"
    )
    wrap_solved_days_with_links(
        month_soup,
        month_soup,
        dir_date.year,
        dir_date.month,
        lambda idx: f"{idx:%Y%m%d}.py",
        solved_files_by_date,
    )
    month_soup.table["align"] = "center"
    readme_content = month_soup.prettify()

    print(f"Writing {readme}")
    readme.write_text(readme_content)

root_year_sections = []
for year in sorted(solved_months_by_year):
    year_dir = BASE_SOLUTIONS_DIR / str(year)
    year_readme = year_dir / "README.md"
    year_html = build_year_calendar_html(
        year=year,
        months=sorted(solved_months_by_year[year]),
        href_func=lambda idx, year=year: f"{idx:%Y%m}/{idx:%Y%m%d}.py",
        solved_dates=solved_files_by_date,
    )

    print(f"Writing {year_readme}")
    year_readme.write_text(year_html)

    root_year_html = build_year_calendar_html(
        year=year,
        months=sorted(solved_months_by_year[year]),
        href_func=lambda idx: f"solutions/{idx:%Y}/{idx:%Y%m}/{idx:%Y%m%d}.py",
        solved_dates=solved_files_by_date,
    )
    root_year_sections.append(f"### {year}\n\n{root_year_html}")

replace_or_append_root_calendar_section("\n\n".join(root_year_sections))
