# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


class Solution:
    """1877. Minimize Maximum Pair Sum in Array

    The **pair sum** of a pair `(a,b)` is equal to `a + b`. The **maximum pair sum** is
    the largest **pair sum** in a list of pairs.

    * For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the **maximum pair
    sum** would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

    Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n
    / 2` pairs such that:

    * Each element of `nums` is in **exactly one** pair, and

    * The **maximum pair sum** is **minimized**.

    Return *the minimized **maximum pair sum** after optimally pairing up the elements*.

    Constraints:
        * `n == nums.length`
        * `2 <= n <= 105`
        * `n` is even.
        * `1 <= nums[i] <= 105`
    """

    def min_pair_sum(self, nums: list[int]) -> int:
        """The minimized maximum pair sum after optimally pairing up the elements.

        Accomplished by sorting the input and then pairing the elements from both ends.

        Args:
            nums: The input integer list.

        Returns:
            The maximum pair sum of the input.
        """
        # Sort the array in ascending order.
        nums.sort()
        n = len(nums)
        result = 0

        # Pair the smallest and largest elements, the second smallest and second
        # largest elements, and so on.
        for i in range(n // 2):
            result = max(result, nums[i] + nums[n - 1 - i])

        return result

    minPairSum = min_pair_sum
