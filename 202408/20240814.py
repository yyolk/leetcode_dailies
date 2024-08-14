# https://leetcode.com/problems/find-k-th-smallest-pair-distance/


class Solution:
    """719. Find K-th Smallest Pair Distance

    The **distance of a pair** of integers `a` and `b` is defined as the absolute
    difference between `a` and `b`.

    Given an integer array `nums` and an integer `k`, return *the* `kth` *smallest
    **distance among all the pairs*** `nums[i]` *and* `nums[j]` *where* `0 <= i < j <
    nums.length`.

    """

    def smallest_distance_pair(self, nums: list[int], k: int) -> int: ...

    smallestDistancePair = smallest_distance_pair
