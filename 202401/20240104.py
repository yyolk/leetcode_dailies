# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
from collections import Counter


class Solution:
    """2870. Minimum Number of Operations to Make Array Empty

    You are given a **0-indexed** array `nums` consisting of positive integers.

    There are two types of operations that you can apply on the array **any** number of
    times:

    * Choose **two** elements with **equal** values and **delete** them from the array.

    * Choose **three** elements with **equal** values and **delete** them from the
    array.

    Return *the **minimum** number of operations required to make the array empty, or*
    `-1` *if it is not possible*.
    """

    def min_operations(self, nums: list[int]) -> int:
        # Count the occurrences of each element in the array
        mp = Counter(nums)

        # Initialize a variable to count the operations
        count = 0

        # Iterate through the occurrences of each element in the Counter
        for t in mp.values():
            # If there is only one occurrence of an element, it's not possible to
            # perform operations.
            if t == 1:
                return -1

            # Calculate the number of three-element operations and update the count
            count += t // 3

            # If there are remaining elements, perform a two-element operation
            if t % 3:
                count += 1

        # Return the total count of operations
        return count

    minOperations = min_operations
