# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/


class Solution:
    """3375. Minimum Operations to Make Array Values Equal to K

    You are given an integer array `nums` and an integer `k`.

    An integer `h` is called **valid** if all values in the array that are **strictly
    greater** than `h` are *identical*.

    For example, if `nums = [10, 8, 10, 8]`, a **valid** integer is `h = 9` because all
    `nums[i] > 9` are equal to 10, but 5 is not a **valid** integer.

    You are allowed to perform the following operation on `nums`:

    * Select an integer `h` that is *valid* for the **current** values in `nums`.

    * For each index `i` where `nums[i] > h`, set `nums[i]` to `h`.

    Return the **minimum** number of operations required to make every element in `nums`
    **equal** to `k`. If it is impossible to make all elements equal to `k`, return -1.
    """

    def min_operations(self, nums: list[int], k: int) -> int:
        # Check if any element is less than k
        if any(num < k for num in nums):
            return -1
        # Collect distinct values greater than k
        greater_than_k = set(num for num in nums if num > k)
        # Return the number of distinct values greater than k
        return len(greater_than_k)

    minOperations = min_operations
