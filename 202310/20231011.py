# https://leetcode.com/problems/number-of-flowers-in-full-bloom/


class Solution:
    """2251. Number of Flowers in Full Bloom

    You are given a **0-indexed** 2D integer array `flowers`, where `flowers[i] =
    [starti, endi]` means the `ith` flower will be in **full bloom** from `starti` to
    `endi` (**inclusive**). You are also given a **0-indexed** integer array `people` of
    size `n`, where `people[i]` is the time that the `ith` person will arrive to see the
    flowers.

    Return *an integer array* `answer` *of size* `n`*, where* `answer[i]` *is the
    **number** of flowers that are in full bloom when the* `ith` *person arrives.*
    """

    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        ...
