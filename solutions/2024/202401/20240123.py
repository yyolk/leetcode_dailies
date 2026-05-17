# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


class Solution:
    """1239. Maximum Length of a Concatenated String with Unique Characters

    You are given an array of strings `arr`. A string `s` is formed by the
    **concatenation** of a **subsequence** of `arr` that has **unique characters**.

    Return *the **maximum** possible length* of `s`.

    A **subsequence** is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    """

    def max_length(self, arr: list[str]) -> int:
        max_length = 0

        def is_unique(subseq):
            return len(subseq) == len(set(subseq))

        def backtrack(start, current):
            nonlocal max_length

            max_length = max(max_length, len(current))

            for i in range(start, len(arr)):
                if is_unique(current + arr[i]):
                    backtrack(i + 1, current + arr[i])

        backtrack(0, "")
        return max_length

    maxLength = max_length
