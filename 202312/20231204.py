# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
import re


CONTIGUOUS_DIGIT_PATTERN = re.compile(r"(\d)\1{2}")


class Solution:
    """2264. Largest 3-Same-Digit Number in String

    You are given a string `num` representing a large integer. An integer is **good** if
    it meets the following conditions:

    * It is a **substring** of `num` with length `3`.

    * It consists of only one unique digit.

    Return *the **maximum good** integer as a **string** or an empty string* `""` *if no
    such integer exists*.

    Note:

    * A **substring** is a contiguous sequence of characters within a string.

    * There may be **leading zeroes** in `num` or a good integer.
    """

    def largest_good_integer(self, num: str) -> str:
        """Finds the largest good integer.

        Args:
            num: Input string to scan for a good integer.

        Returns:
            The largest, good integer as a string if it exists,
                "" if no good integer exists.
        """
        all_digits_found = CONTIGUOUS_DIGIT_PATTERN.findall(num)
        if all_digits_found:
            largest_good_integer = max(all_digits_found, key=int)
            return largest_good_integer * 3
        else:
            return ""

    largestGoodInteger = largest_good_integer
