# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from collections import Counter


class Solution:
    """442. Find All Duplicates in an Array

    Given an integer array `nums` of length `n` where all the integers of `nums` are in
    the range `[1, n]` and each integer appears **once** or **twice**, return *an array
    of all the integers that appears **twice***.

    You must write an algorithm that runs in `O(n)`time and uses only constant extra
    space.

    """

    def find_duplicates(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        return [num for num, count in counter.items() if count == 2]

    findDuplicates = find_duplicates
