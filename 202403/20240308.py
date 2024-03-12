# https://leetcode.com/problems/count-elements-with-maximum-frequency/
from collections import Counter


class Solution:
    """3005. Count Elements With Maximum Frequency

    You are given an array nums consisting of positive integers.

    Return the total frequencies of elements in nums such that those elements all have
    the maximum frequency.

    The frequency of an element is the number of occurrences of that element in the array.
    """

    def max_frequency_elements(self, nums: list[int]) -> int:
        # Check for empty input
        if not nums:
            return 0

        # Count the frequency of each element
        frequency_counter = Counter(nums)

        # Find the maximum frequency
        max_frequency = max(frequency_counter.values())

        # Calculate the total frequencies of elements with the maximum frequency
        total_frequency = sum(
            count for count in frequency_counter.values() if count == max_frequency
        )

        return total_frequency

    maxFrequencyElements = max_frequency_element
