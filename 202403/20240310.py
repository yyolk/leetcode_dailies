# https://leetcode.com/problems/intersection-of-two-arrays/


class Solution:
    """349. Intersection of Two Arrays
    
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    
    Each element in the result must be unique and you may return the result in any order.
    """
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Use set intersection and return a list.
        return list(set(nums1) & set(nums2))