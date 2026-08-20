# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/


class Solution:
    """3069. Distribute Elements Into Two Arrays I

    You are given a **1-indexed** array of **distinct** integers `nums` of length `n`.

    You need to distribute all the elements of `nums` between two arrays `arr1` and
    `arr2` using `n` operations. In the first operation, append `nums[1]` to `arr1`. In
    the second operation, append `nums[2]` to `arr2`. Afterwards, in the `ith`
    operation:

    * If the last element of `arr1` is **greater** than the last element of `arr2`,
    append `nums[i]` to `arr1`. Otherwise, append `nums[i]` to `arr2`.

    The array `result` is formed by concatenating the arrays `arr1` and `arr2`. For
    example, if `arr1 == [1,2,3]` and `arr2 == [4,5,6]`, then `result = [1,2,3,4,5,6]`.

    Return *the array* `result`.

    Constraints:

    * `3 <= n <= 50`

    * `1 <= nums[i] <= 100`

    * All elements in `nums` are distinct."""

    def result_array(self, nums: list[int]) -> list[int]:
        """Return the result array built by appending to arr1/arr2 by last-value rule."""
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for value in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(value)
            else:
                arr2.append(value)

        return arr1 + arr2

    resultArray = result_array
