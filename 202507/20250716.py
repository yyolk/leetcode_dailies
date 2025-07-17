# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/


class Solution:
    """3201. Find the Maximum Length of Valid Subsequence I

    You are given an integer array `nums`.

    A subsequence `sub` of `nums` with length `x` is called **valid** if it satisfies:

    * `(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x -
    1]) % 2.`

    Return the length of the **longest** **valid** subsequence of `nums`.

    A **subsequence** is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements."""

    def maximum_length(self, nums: list[int]) -> int:
        # Handle empty input case
        if not nums:
            return 0
        # Count the number of even numbers
        count_even = sum(1 for x in nums if x % 2 == 0)
        # Count the number of odd numbers
        count_odd = len(nums) - count_even
        # Maximum length for all same parity subsequence
        max_same = max(count_even, count_odd)

        # Initialize DP for longest alternating ending with even
        dp_even = 0
        # Initialize DP for longest alternating ending with odd
        dp_odd = 0
        # Iterate through each number
        for num in nums:
            # If number is even
            if num % 2 == 0:
                # Update dp_even: continue from dp_even or extend from dp_odd
                dp_even = max(dp_even, dp_odd + 1)
            # If number is odd
            else:
                # Update dp_odd: continue from dp_odd or extend from dp_even
                dp_odd = max(dp_odd, dp_even + 1)

        # Maximum length for alternating parity subsequence
        max_alt = max(dp_even, dp_odd)
        # Return the overall maximum
        return max(max_same, max_alt)

    maximumLength = maximum_length
