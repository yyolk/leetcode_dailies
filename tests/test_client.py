"""Tests for generate_active_daily.client module."""

import asyncio

from generate_active_daily.client import make_leetcode_url_from_slug, previous_questions


class TestMakeLeetcodeUrlFromSlug:
    def test_simple_slug(self):
        url = make_leetcode_url_from_slug("two-sum")
        assert url == "https://leetcode.com/problems/two-sum/"

    def test_multi_word_slug(self):
        url = make_leetcode_url_from_slug("valid-parentheses")
        assert url == "https://leetcode.com/problems/valid-parentheses/"

    def test_long_slug(self):
        url = make_leetcode_url_from_slug("find-median-from-data-stream")
        assert url == "https://leetcode.com/problems/find-median-from-data-stream/"

    def test_url_starts_with_base(self):
        url = make_leetcode_url_from_slug("any-slug")
        assert url.startswith("https://leetcode.com/problems/")

    def test_url_ends_with_slash(self):
        url = make_leetcode_url_from_slug("any-slug")
        assert url.endswith("/")


class TestPreviousQuestions:
    def test_zero_limit_yields_nothing(self):
        async def collect():
            results = []
            async for q in previous_questions(0):
                results.append(q)
            return results

        results = asyncio.run(collect())
        assert results == []

    def test_negative_limit_yields_nothing(self):
        async def collect():
            results = []
            async for q in previous_questions(-5):
                results.append(q)
            return results

        results = asyncio.run(collect())
        assert results == []
