# https://leetcode.com/problems/largest-odd-number-in-string/


class Solution:
    """1903. Largest Odd Number in String

    You are given a string `num`, representing a large integer. Return *the **largest-
    valued odd** integer (as a string) that is a **non-empty substring** of* `num`*, or
    an empty string* `""` *if no odd integer exists*.

    A **substring** is a contiguous sequence of characters within a string.
    """

    def largest_odd_number(self, num: str) -> str:
        """Find the largest odd number in the input.

        Iterating backwards will always find the largest odd substring once an odd
        substring is encountered.

        Instead of using moduluo 2 against the int(number: str) to deterimine if it's odd,
        we can just see if our encountered ``digit: str`` is any of the odd numbers 1-9.

        Compare using a literal sequence of odd numbers 1-9, ``"13579"``.

        Args:
            num: Input string to search.

        Returns:
            The largest-valued odd integer, or "" if no odd integer exists.
        """
        # Iterate over all input characters (digits), backwards.
        for i in range(len(num) - 1, -1, -1):
            # Determine if it's odd, if any of these digits are num[i].
            if num[i] in "13579":
                # Make our substring up to i, inclusive.
                return num[: i + 1]

        # No odd substring found.
        return ""

    largestOddNumber = largest_odd_number
