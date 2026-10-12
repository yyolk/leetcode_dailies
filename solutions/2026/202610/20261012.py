# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/


class Solution:
    """2897. Apply Operations on Array to Maximize Sum of Squares

    You are given a **0-indexed** integer array `nums` and a **positive** integer `k`.

    You can do the following operation on the array **any** number of times:

    * Choose any two distinct indices `i` and `j` and **simultaneously** update the
    values of `nums[i]` to `(nums[i] AND nums[j])` and `nums[j]` to `(nums[i] OR
    nums[j])`. Here, `OR` denotes the bitwise `OR` operation, and `AND` denotes the
    bitwise `AND` operation.

    You have to choose `k` elements from the final array and calculate the sum of their
    **squares**.

    Return *the **maximum** sum of squares you can achieve*.

    Since the answer can be very large, return it **modulo** `109 + 7`.

    Constraints:

    * `1 <= k <= nums.length <= 105`

    * `1 <= nums[i] <= 109`"""

    def max_sum(self, nums: list[int], k: int) -> int:
        """...

        Proposed solution ...

        Args:
            nums (list of int): ...
            k (int): ...

        Returns:
            int: ..."""
        ...

    maxSum = max_sum
