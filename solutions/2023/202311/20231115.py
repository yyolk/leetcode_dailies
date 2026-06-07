# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/


class Solution:
    """1846. Maximum Element After Decreasing and Rearranging

    You are given an array of positive integers `arr`. Perform some operations (possibly
    none) on `arr` so that it satisfies these conditions:

    * The value of the **first** element in `arr` must be `1`.

    * The absolute difference between any 2 adjacent elements must be **less than or
    equal to** `1`. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where
    `1 <= i < arr.length` (**0-indexed**). `abs(x)` is the absolute value of `x`.

    There are 2 types of operations that you can perform any number of times:

    * **Decrease** the value of any element of `arr` to a **smaller positive integer**.

    * **Rearrange** the elements of `arr` to be in any order.

    Return *the **maximum** possible value of an element in* `arr` *after performing the
    operations to satisfy the conditions*.
    """

    def maximum_element_after_decrementing_and_rearranging(self, arr: list[int]) -> int:
        """Maximum possible value of an element in arr after performing the operations.

        Args:
            arr: The input array of integers to perform operations on.

        Returns:
            The maximum possible value after performing the operations.
        """
        # Initialize the condition with 1.
        max_possible = 1

        # Adjust each element after sorting to satisfy the conditions while maximizing
        # its value.
        for i in sorted(arr)[1:]:
            # Update the maximum possible value based on the conditions.
            if i > max_possible:
                max_possible += 1

        return max_possible

    maximumElementAfterDecrementingAndRearranging = (
        maximum_element_after_decrementing_and_rearranging
    )
