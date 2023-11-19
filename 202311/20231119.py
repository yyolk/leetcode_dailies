# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
from collections import Counter


class Solution:
    """1887. Reduction Operations to Make the Array Elements Equal

    Given an integer array `nums`, your goal is to make all elements in `nums` equal. To
    complete one operation, follow these steps:

    1. Find the **largest** value in `nums`. Let its index be `i` (**0-indexed**) and
    its value be `largest`. If there are multiple elements with the largest value, pick
    the smallest `i`.

    2. Find the **next largest** value in `nums` **strictly smaller** than `largest`.
    Let its value be `nextLargest`.

    3. Reduce `nums[i]` to `nextLargest`.

    Return *the number of operations to make all elements in* `nums` *equal*.
    """

    def reduction_operations(self, nums: list[int]) -> int:
        """The number of operations to make all elements equal.

        Args:
            nums: The list of integers to make all equal.

        Returns:
            The number of operations it took to make all elements equal.
        """
        # Count occurrences of each unique number.
        counter_dict = Counter(nums)

        # Sort the counts and enumerate them.
        sorted_counts = sorted(counter_dict.items())

        # Calculate the number of operations using a generator expression.
        return sum(i * cnt for i, (_, cnt) in enumerate(sorted_counts))

    reductionOperations = reduction_operations
