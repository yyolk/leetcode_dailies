# https://leetcode.com/problems/minimum-index-of-a-valid-split/


class Solution:
    """2780. Minimum Index of a Valid Split

    An element `x` of an integer array `arr` of length `m` is **dominant** if **more
    than half** the elements of `arr` have a value of `x`.

    You are given a **0-indexed** integer array `nums` of length `n` with one
    **dominant** element.

    You can split `nums` at an index `i` into two arrays `nums[0, ..., i]` and `nums[i +
    1, ..., n - 1]`, but the split is only **valid** if:

    * `0 <= i < n - 1`

    * `nums[0, ..., i]`, and `nums[i + 1, ..., n - 1]` have the same dominant element.

    Here, `nums[i, ..., j]` denotes the subarray of `nums` starting at index `i` and
    ending at index `j`, both ends being inclusive. Particularly, if `j < i` then
    `nums[i, ..., j]` denotes an empty subarray.

    Return *the **minimum** index of a **valid split***. If no valid split exists,
    return `-1`."""

    def minimum_index(self, nums: list[int]) -> int:
        n = len(nums)
        # If n < 2, no split is possible since we need i < n-1 and i >= 0
        if n < 2:
            return -1

        # Step 1: Find the dominant element using Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        D = candidate

        # Step 2: Count total occurrences of the dominant element D
        total_D = 0
        for num in nums:
            if num == D:
                total_D += 1

        # Step 3: Find the minimum index i where both parts have D as dominant
        running_count = 0
        for i in range(n - 1):
            if nums[i] == D:
                running_count += 1
            # Check if D is dominant in both left part [0..i] and right part [i+1..n-1]
            if (
                running_count > (i + 1) // 2
                and (total_D - running_count) > (n - i - 1) // 2
            ):
                return i

        # If no valid split is found, return -1
        return -1

    minimumIndex = minimum_index
