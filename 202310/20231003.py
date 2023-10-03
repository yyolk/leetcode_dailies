# https://leetcode.com/problems/number-of-good-pairs/
from collections import Counter


class Solution:
    """1512. Number of Good Pairs

    Given an array of integers `nums`, return *the number of **good pairs***.

    A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i` < `j`.
    """

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """How many identical pairs, which are good are in the input

        Proposed solution using one loop and a collections.Counter for the occurences.

        Args:
            nums (List of int): The input list of numbers to scan for good pairs.

        Returns:
            int: The number of good pairs found in the input.
        """
        # Create a counter to count the occurences of each element
        counter = Counter()

        # Initialize the count of good pairs
        count = 0

        # Iterate through the input list
        for num in nums:
            # If the number is already in the counter, increment the count
            if num in counter:
                count += counter[num]

            # Increment the count of this number in the counter
            counter[num] += 1

        return count
