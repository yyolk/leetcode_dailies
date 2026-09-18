# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/


class Solution:
    """1520. Maximum Number of Non-Overlapping Substrings

    Given a string `s` of lowercase letters, you need to find the maximum number of
    **non-empty** substrings of `s` that meet the following conditions:

    1. The substrings do not overlap, that is for any two substrings `s[i..j]` and
    `s[x..y]`, either `j < x` or `i > y` is true.

    2. A substring that contains a certain character `c` must also contain all
    occurrences of `c`.

    Find *the maximum number of substrings that meet the above conditions*. If there
    are multiple solutions with the same number of substrings, *return the one with
    minimum total length.* It can be shown that there exists a unique solution of
    minimum total length.

    Notice that you can return the substrings in **any** order.

    Constraints:

    * `1 <= s.length <= 105`

    * `s` contains only lowercase English letters.
    """

    def max_num_of_substrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == n:
                first[idx] = i
            last[idx] = i

        def close_interval(start: int) -> int:
            # Grow [start, end] until every letter inside is fully contained.
            end = last[ord(s[start]) - 97]
            j = start
            while j <= end:
                left = first[ord(s[j]) - 97]
                if left < start:
                    return -1
                end = max(end, last[ord(s[j]) - 97])
                j += 1
            return end

        answer: list[str] = []
        prev_end = -1
        for i, ch in enumerate(s):
            # Only start a candidate at a letter's first occurrence.
            if i != first[ord(ch) - 97]:
                continue
            new_end = close_interval(i)
            if new_end < 0:
                continue
            # Nested valid interval: replace last pick to minimize total length.
            if i <= prev_end and answer:
                answer[-1] = s[i : new_end + 1]
            else:
                answer.append(s[i : new_end + 1])
            prev_end = new_end
        return answer

    maxNumOfSubstrings = max_num_of_substrings
