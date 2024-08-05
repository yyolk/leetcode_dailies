# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
MOD = 10**9 + 7


class Solution:
    """1508. Range Sum of Sorted Subarray Sums

    You are given the array `nums` consisting of `n` positive integers. You computed the
    sum of all non\\-empty continuous subarrays from the array and then sorted them in
    non\\-decreasing order, creating a new array of `n * (n + 1) / 2` numbers.

    *Return the sum of the numbers from index* `left` *to index* `right` (**indexed from
    1**)*, inclusive, in the new array.* Since the answer can be a huge number return it
    modulo `109 + 7`.

    """

    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:

        # Step 1: Generate all possible subarray sums
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        # Step 2: Sort the subarray sums
        subarray_sums.sort()

        # Step 3: Calculate the sum of elements from `left` to `right` (1-based index)
        range_sum = sum(subarray_sums[left - 1 : right]) % MOD

        return range_sum

    rangeSum = range_sum
