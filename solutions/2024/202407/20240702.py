# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter


class Solution:
    """350. Intersection of Two Arrays II

    Given two integer arrays `nums1` and `nums2`, return *an array of their
    intersection*. Each element in the result must appear as many times as it shows in
    both arrays and you may return the result in **any order**.

    """

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Count the occurrences of each element in nums1
        counts = Counter(nums1)

        # Result array to store the intersection
        result = []

        # Iterate through nums2 and add common elements to the result
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

    intersect = intersect
