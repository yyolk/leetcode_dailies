"""Generate calendar TOCs for month dirs, year dirs, and the root README."""

import calendar
import re

from collections import defaultdict
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

BASE_SOLUTIONS_DIR = Path("solutions")
MONTH_DIR_PATTERN = re.compile(r"^\d{6}$")
FILE_PATTERN = re.compile(r"^\d{8}\.py$")
DAYS_PATTERN = re.compile(r"^\d+$")
ROOT_README_PATH = Path("README.md")
ROOT_CALENDAR_SECTION_HEADER = "## Solutions Calendar"
ROOT_CALENDAR_START = "<!-- SOLUTIONS_CALENDAR_START -->"
ROOT_CALENDAR_END = "<!-- SOLUTIONS_CALENDAR_END -->"


def month_name_to_num(month_name):
    """Map month names like 'January' to 1, etc."""
    return list(calendar.month_name).index(month_name)


def wrap_solved_days_with_links(table, root_soup, year, month, href_func, solved_dates):
    """Link solved days in a month table."""
    for el in table.find_all("td", string=DAYS_PATTERN):
        day = int(el.get_text())
        idx = datetime(year=year, month=month, day=day)
        if idx in solved_dates:
            el.string.wrap(root_soup.new_tag("a", href=href_func(idx)))


def build_year_calendar_html(year, href_func, solved_dates, months=None):
    """Build a year HTML calendar with linked solved days."""
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    soup = BeautifulSoup(cal.formatyear(year, width=2), "html.parser")
    months_to_render = set(months or range(1, 13))

    for month_table in soup.find_all("table", class_="month"):
        month_header = month_table.find("th", class_="month")
        if month_header is None:
            continue
        month = month_name_to_num(month_header.get_text(strip=True))
        if month not in months_to_render:
            month_container = month_table.find_parent("td")
            if month_container is None:
                month_table.decompose()
            else:
                month_container.decompose()
            continue
        wrap_solved_days_with_links(
            month_table, soup, year, month, href_func, solved_dates
        )

    if soup.table:
        for row in soup.table.find_all("tr", recursive=False):
            if row.find("th", class_="year"):
                continue
            if not row.find("table", class_="month"):
                row.decompose()

    if soup.table:
        soup.table["align"] = "center"

    return soup.prettify()


def replace_or_append_root_calendar_section(section):
    """Replace generated section in root README, or append it if missing."""
    readme_content = ROOT_README_PATH.read_text()
    generated = (
        f"{ROOT_CALENDAR_SECTION_HEADER}\n\n"
        f"{ROOT_CALENDAR_START}\n\n{section}\n{ROOT_CALENDAR_END}\n"
    )

    if ROOT_CALENDAR_START in readme_content and ROOT_CALENDAR_END in readme_content:
        before, after_start = readme_content.split(ROOT_CALENDAR_START, maxsplit=1)
        _, after = after_start.split(ROOT_CALENDAR_END, maxsplit=1)
        updated = (
            f"{before}{ROOT_CALENDAR_START}\n\n{section}\n{ROOT_CALENDAR_END}{after}"
        )
    else:
        separator = "" if readme_content.endswith("\n") else "\n"
        updated = f"{readme_content}{separator}\n{generated}"

    print(f"Writing {ROOT_README_PATH}")
    ROOT_README_PATH.write_text(updated)


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
