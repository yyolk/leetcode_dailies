# https://leetcode.com/problems/sort-array-by-increasing-frequency/
from collections import Counter


class Solution:
    """1636. Sort Array by Increasing Frequency

    Given an array of integers `nums`, sort the array in **increasing** order based on
    the frequency of the values. If multiple values have the same frequency, sort them
    in **decreasing** order.

    Return the *sorted array*.

    """

    def frequency_sort(self, nums: list[int]) -> list[int]:
        # Count the frequency of each value in the array
        freq = Counter(nums)
        
        # Sort the values based on frequency (ascending) and value (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums

    frequencySort = frequency_sort
