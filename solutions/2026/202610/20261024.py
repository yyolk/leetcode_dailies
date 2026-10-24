# https://leetcode.com/problems/count-days-spent-together/


class Solution:
    """2409. Count Days Spent Together

    Alice and Bob are traveling to Rome for separate business meetings.

    You are given 4 strings `arrive_alice`, `leave_alice`, `arrive_bob`, and
    `leave_bob`. Alice will be in the city from the dates `arrive_alice` to
    `leave_alice` (**inclusive**), while Bob will be in the city from the dates
    `arrive_bob` to `leave_bob` (**inclusive**). Each will be a 5-character string in
    the format `"MM-DD"`, corresponding to the month and day of the date.

    Return *the total number of days that Alice and Bob are in Rome together.*

    You can assume that all dates occur in the **same** calendar year, which is **not**
    a leap year. Note that the number of days per month can be represented as: `[31, 28,
    31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.

    Constraints:

    * All dates are provided in the format `"MM-DD"`.

    * Alice and Bob's arrival dates are **earlier than or equal to** their leaving
    dates.

    * The given dates are valid dates of a **non-leap** year."""

    def count_days_together(
        self, arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str
    ) -> int:
        """...

        Proposed solution ...

        Args:
            arrive_alice (str): ...
            leave_alice (str): ...
            arrive_bob (str): ...
            leave_bob (str): ...

        Returns:
            int: ..."""
        ...

    countDaysTogether = count_days_together
