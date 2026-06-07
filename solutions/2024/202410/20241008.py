# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/


class Solution:
    """1963. Minimum Number of Swaps to Make the String Balanced

    You are given a **0\\-indexed** string `s` of **even** length `n`. The string
    consists of **exactly** `n / 2` opening brackets `"["` and `n / 2` closing brackets
    `"]"`.

    A string is called **balanced** if and only if:

    * It is the empty string, or

    * It can be written as `AB`, where both `A` and `B` are **balanced** strings, or

    * It can be written as `[C]`, where `C` is a **balanced** string.

    You may swap the brackets at **any** two indices **any** number of times.

    Return *the **minimum** number of swaps to make* `s` ***balanced***.

    """

    def min_swaps(self, s: str) -> int:
        misplaced_closing = 0
        open_count = 0

        for bracket in s:
            if bracket == "[":
                open_count += 1
            else:  # bracket == "]"
                if open_count == 0:
                    # We"ve found a closing bracket with no matching opening bracket before it
                    misplaced_closing += 1
                else:
                    open_count -= 1

        # Each misplaced pair needs one swap to fix, but since one swap can fix two brackets,
        # we divide by 2. We also add 1 before division to handle odd numbers correctly by rounding up.
        return (misplaced_closing + 1) // 2

    minSwaps = min_swaps
