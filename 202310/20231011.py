# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
from bisect import bisect_left, bisect_right


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
        """The number of flowers in full bloom when the ith person arrives.

        Proposed solution via MrAke:
        https://leetcode.com/problems/number-of-flowers-in-full-bloom/solutions/4155347/97-44-easy-3-line-solution-with-explanation/

        Args:
            flowers (List of List of int): A 0-indexed 2D integer array where
                `flowers_i = [start_i, end_i]` means the ith flower will be in full
                bloom from `start_i` to `end_i`.
            people (List of int): A 0-indexed integer array where people[i] is the time
                that the ith person will arrive to see the flowers.

        Returns:
            List of int: An integer array where i is the number of flowers that are in
            full bloom when the ith person arrives.
        """
        # Extract the start and end times of flower intervals
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])

        # Initialize our result list for storing the count of flowers infull bloom
        result = []

        for t in people:
            # Use bisect functions to find the count of flowers in full bloom
            count = bisect_right(start, t) - bisect_left(end, t)
            result.append(count)

        return result
