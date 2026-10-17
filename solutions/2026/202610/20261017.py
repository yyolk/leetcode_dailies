# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/


class Solution:
    """3551. Minimum Swaps to Sort by Digit Sum

    You are given an array nums of distinct positive integers. You need to sort
    the array in increasing order based on the sum of the digits of each number.
    If two numbers have the same digit sum, the smaller number appears first in
    the sorted order.

    Return the minimum number of swaps required to rearrange nums into this
    sorted order.

    A swap is defined as exchanging the values at two distinct positions in the
    array.

    Constraints:

    * 1 <= nums.length <= 10**5

    * 1 <= nums[i] <= 10**9

    * nums consists of distinct positive integers.
    """

    def min_swaps(self, nums: list[int]) -> int:
        # Digit sum helper: sum of decimal digits.
        def digit_sum(num: int) -> int:
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        n = len(nums)
        # Sort by (digit_sum, value) to get the target order.
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        # Map each value to its target index in the sorted order.
        target_index = {value: i for i, value in enumerate(sorted_nums)}

        visited = [False] * n
        cycles = 0
        # Count cycles in the permutation of positions.
        for i in range(n):
            if visited[i]:
                continue
            # Walk the cycle starting at i.
            j = i
            while not visited[j]:
                visited[j] = True
                # Follow where the current value should go.
                j = target_index[nums[j]]
            cycles += 1

        # Minimum swaps is n minus the number of cycles.
        return n - cycles

    minSwaps = min_swaps
