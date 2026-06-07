"""Tests for generate_calendar_toc.utils module."""

import calendar

from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from bs4 import BeautifulSoup

from generate_calendar_toc.utils import (
    ROOT_CALENDAR_END,
    ROOT_CALENDAR_SECTION_HEADER,
    ROOT_CALENDAR_START,
    build_year_calendar_html,
    month_name_to_num,
    replace_or_append_root_calendar_section,
    wrap_solved_days_with_links,
)


class TestMonthNameToNum:
    def test_january(self):
        assert month_name_to_num("January") == 1

    def test_december(self):
        assert month_name_to_num("December") == 12

    def test_june(self):
        assert month_name_to_num("June") == 6

    def test_all_months(self):
        for i, name in enumerate(calendar.month_name[1:], start=1):
            assert month_name_to_num(name) == i


class TestWrapSolvedDaysWithLinks:
    def _make_month_soup(self, year, month):
        cal = calendar.HTMLCalendar(calendar.SUNDAY)
        return BeautifulSoup(cal.formatmonth(year, month), "html.parser")

    def test_no_solved_dates_no_links(self):
        soup = self._make_month_soup(2024, 1)
        wrap_solved_days_with_links(soup, soup, 2024, 1, lambda idx: "#", {})
        # No anchor tags should be present
        assert soup.find("a") is None

    def test_solved_date_gets_link(self):
        soup = self._make_month_soup(2024, 1)
        solved = {datetime(2024, 1, 15): Path("solutions/2024/202401/20240115.py")}
        wrap_solved_days_with_links(
            soup, soup, 2024, 1, lambda idx: f"{idx:%Y%m%d}.py", solved
        )
        link = soup.find("a")
        assert link is not None
        assert link["href"] == "20240115.py"
        assert link.get_text() == "15"

    def test_only_solved_days_linked(self):
        soup = self._make_month_soup(2024, 3)
        solved = {
            datetime(2024, 3, 1): Path("x"),
            datetime(2024, 3, 31): Path("y"),
        }
        wrap_solved_days_with_links(
            soup, soup, 2024, 3, lambda idx: f"{idx:%Y%m%d}.py", solved
        )
        links = soup.find_all("a")
        assert len(links) == 2
        link_texts = {a.get_text() for a in links}
        assert link_texts == {"1", "31"}

    def test_href_func_called_with_correct_date(self):
        soup = self._make_month_soup(2024, 6)
        called_with = []
        solved = {datetime(2024, 6, 10): Path("x")}
        wrap_solved_days_with_links(
            soup, soup, 2024, 6, lambda idx: called_with.append(idx) or "#", solved
        )
        assert called_with == [datetime(2024, 6, 10)]


class TestBuildYearCalendarHtml:
    def test_returns_string(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {})
        assert isinstance(result, str)

    def test_contains_year(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {})
        assert "2024" in result

    def test_all_months_present_by_default(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {})
        for name in calendar.month_name[1:]:
            assert name in result

    def test_only_specified_months_rendered(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {}, months=[1, 2])
        assert "January" in result
        assert "February" in result
        assert "March" not in result
        assert "December" not in result

    def test_solved_day_has_link(self):
        solved = {datetime(2024, 5, 20): Path("x")}
        result = build_year_calendar_html(
            2024, lambda idx: f"{idx:%Y%m%d}.py", solved, months=[5]
        )
        assert "20240520.py" in result

    def test_table_has_center_align(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {}, months=[1])
        soup = BeautifulSoup(result, "html.parser")
        table = soup.find("table")
        assert table is not None
        assert table.get("align") == "center"

    def test_empty_months_list_uses_all(self):
        result = build_year_calendar_html(2024, lambda idx: "#", {}, months=None)
        for name in calendar.month_name[1:]:
            assert name in result


class TestReplaceOrAppendRootCalendarSection:
    def test_appends_when_section_absent(self, tmp_path):
        readme = tmp_path / "README.md"
        readme.write_text("# My Project\n\nSome content.\n")
        with patch("generate_calendar_toc.utils.ROOT_README_PATH", readme):
            replace_or_append_root_calendar_section("Calendar content here")
        content = readme.read_text()
        assert ROOT_CALENDAR_START in content
        assert ROOT_CALENDAR_END in content
        assert "Calendar content here" in content
        assert ROOT_CALENDAR_SECTION_HEADER in content

    def test_replaces_existing_section(self, tmp_path):
        readme = tmp_path / "README.md"
        readme.write_text(
            f"# Header\n\n{ROOT_CALENDAR_START}\n\nOld content\n{ROOT_CALENDAR_END}\n"
        )
        with patch("generate_calendar_toc.utils.ROOT_README_PATH", readme):
            replace_or_append_root_calendar_section("New content")
        content = readme.read_text()
        assert "New content" in content
        assert "Old content" not in content

    def test_preserves_content_before_section(self, tmp_path):
        readme = tmp_path / "README.md"
        before_text = "# Header\n\nKeep this.\n\n"
        readme.write_text(
            f"{before_text}{ROOT_CALENDAR_START}\n\nOld\n{ROOT_CALENDAR_END}\n"
        )
        with patch("generate_calendar_toc.utils.ROOT_README_PATH", readme):
            replace_or_append_root_calendar_section("New")
        content = readme.read_text()
        assert "Keep this." in content

    def test_preserves_content_after_section(self, tmp_path):
        readme = tmp_path / "README.md"
        readme.write_text(
            f"{ROOT_CALENDAR_START}\n\nOld\n{ROOT_CALENDAR_END}\n\nAfter content.\n"
        )
        with patch("generate_calendar_toc.utils.ROOT_README_PATH", readme):
            replace_or_append_root_calendar_section("New")
        content = readme.read_text()
        assert "After content." in content

    def test_appends_separator_when_no_trailing_newline(self, tmp_path):
        readme = tmp_path / "README.md"
        readme.write_text("No trailing newline")
        with patch("generate_calendar_toc.utils.ROOT_README_PATH", readme):
            replace_or_append_root_calendar_section("Content")
        content = readme.read_text()
        assert ROOT_CALENDAR_START in content
