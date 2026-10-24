def test_count_days_together_examples(solution):
    # Official Example 1: overlap of 3 days in August.
    assert solution.countDaysTogether("08-15", "08-18", "08-16", "08-19") == 3

    # Official Example 2: no overlapping days.
    assert solution.countDaysTogether("10-01", "10-31", "11-01", "12-31") == 0


def test_count_days_together_single_day(solution):
    # Identical single-day intervals: overlap of 1 day (obvious from spec).
    assert solution.countDaysTogether("01-01", "01-01", "01-01", "01-01") == 1
