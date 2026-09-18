# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/


class Solution:
    """1520. Maximum Number of Non-Overlapping Substrings

    Given a string `s` of lowercase letters, you need to find the maximum number of
    **non-empty** substrings of `s` that meet the following conditions:

    1. The substrings do not overlap, that is for any two substrings `s[i..j]` and
    `s[x..y]`, either `j < x` or `i > y` is true.

    2. A substring that contains a certain character `c` must also contain all
    occurrences of `c`.

    Find *the maximum number of substrings that meet the above conditions*. If there are
    multiple solutions with the same number of substrings, *return the one with minimum
    total length.* It can be shown that there exists a unique solution of minimum total
    length.

    Notice that you can return the substrings in **any** order.

    Constraints:

    * `1 <= s.length <= 105`

    * `s` contains only lowercase English letters."""

    def max_num_of_substrings(self, s: str) -> list[str]:
        """...

        Proposed solution ...

        Args:
            s (str): ...

        Returns:
            list of str: ..."""
        ...

    maxNumOfSubstrings = max_num_of_substrings
