# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/


class Solution:
    """2904. Shortest and Lexicographically Smallest Beautiful String

    You are given a binary string `s` and a positive integer `k`.

    A substring of `s` is **beautiful** if the number of `1`'s in it is exactly `k`.

    Let `len` be the length of the **shortest** beautiful substring.

    Return *the lexicographically **smallest** beautiful substring of string* `s` *with
    length equal to* `len`. If `s` doesn't contain a beautiful substring, return *an
    **empty** string*.

    A string `a` is lexicographically **larger** than a string `b` (of the same length)
    if in the first position where `a` and `b` differ, `a` has a character strictly
    larger than the corresponding character in `b`.

    * For example, `"abcd"` is lexicographically larger than `"abcc"` because the first
    position they differ is at the fourth character, and `d` is greater than `c`.

    Constraints:

    * `1 <= s.length <= 100`

    * `1 <= k <= s.length`"""

    def shortest_beautiful_substring(self, s: str, k: int) -> str:
        """Return shortest, lexicographically smallest substring with exactly ``k`` ones."""
        best = ""
        best_len = len(s) + 1

        for left in range(len(s)):
            ones = 0
            for right in range(left, len(s)):
                if s[right] == "1":
                    ones += 1
                if ones > k:
                    break
                if ones == k:
                    candidate = s[left : right + 1]
                    candidate_len = right - left + 1
                    if candidate_len < best_len or (
                        candidate_len == best_len and candidate < best
                    ):
                        best = candidate
                        best_len = candidate_len
                    break
        return best

    shortestBeautifulSubstring = shortest_beautiful_substring
