# https://leetcode.com/problems/maximum-alternating-sum-of-squares/


class Solution:
    """3727. Maximum Alternating Sum of Squares

    You are given an integer array `nums`. You may **rearrange the elements** in
    any order.

    The **alternating score** of an array `arr` is defined as:

    * `score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...`

    Return an integer denoting the **maximum possible alternating score** of
    `nums` after rearranging its elements.

    Constraints:

    * `1 <= nums.length <= 10^5`

    * `-4 * 10^4 <= nums[i] <= 4 * 10^4`
    """

    def max_alternating_sum(self, nums: list[int]) -> int:
        # Sort by squared magnitude so smaller squares come first.
        # Smallest floor(n/2) squares go to negative positions;
        # remaining larger squares go to positive positions.
        nums.sort(key=lambda x: x * x)
        n = len(nums)
        # Sum of squares of the smaller half (subtracted).
        small_sum = sum(x * x for x in nums[: n // 2])
        # Sum of squares of the larger half (added).
        large_sum = sum(x * x for x in nums[n // 2 :])
        return large_sum - small_sum

    maxAlternatingSum = max_alternating_sum
