# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
from collections import Counter


class Solution:
    """1287. Element Appearing More Than 25% In Sorted Array

    Given an integer array **sorted** in non-decreasing order, there is exactly one
    integer in the array that occurs more than 25% of the time, return that integer.
    """

    def find_special_integer(self, arr: list[int]) -> int:
        """Find the special integer.

        Args:
            arr: The input list of integers to search.

        Returns:
            The one integer in the input that occurs more than 25% of the time.
        """
        # Create a counter instance of all the input integers.
        c = Counter(arr)
        # Get the most_common results list from the counter, and pick off the first
        # element and its first item, which is the integer that occured the most and
        # 25% of the time.
        return c.most_common()[0][0]

    findSpecialInteger = find_special_integer
