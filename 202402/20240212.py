# https://leetcode.com/problems/majority-element/
from collections import Counter


class Solution:
    """169. Majority Element

    Given an array `nums` of size `n`, return *the majority element*.

    The majority element is the element that appears more than `⌊n / 2⌋` times. You may
    assume that the majority element always exists in the array.

    """

    def majority_element(self, nums: list[int]) -> int:
        # Use Counter to count occurrences of each element
        counts = Counter(nums)

        # Use most_common() to get a list of tuples (element, count)
        most_common_elements = counts.most_common()

        # Access the first element of the list to get the element with the highest count
        majority_element = most_common_elements[0][0]

        return majority_element

    majorityElement = majority_element
