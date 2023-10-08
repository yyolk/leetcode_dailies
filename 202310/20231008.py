# https://leetcode.com/problems/max-dot-product-of-two-subsequences/


class Solution:
    """1458. Max Dot Product of Two Subsequences

    Given two arrays `nums1` and `nums2`.

    Return the maximum dot product between **non-empty** subsequences of nums1 and nums2
    with the same length.

    A subsequence of a array is a new array which is formed from the original array by
    deleting some (can be none) of the characters without disturbing the relative positions
    of the remaining characters. (ie, `[2,3,5]` is a subsequence of `[1,2,3,4,5]` while
    `[1,5,3]` is not).
    """

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """Maximum dot product between inputs subsequences.

        Proposed solution using dynamic programming.

        Args:
            nums1 (List of int): Input subsequence 1.
            nums2 (List of int): Input subsequence 2.

        Returns:
            int: Maximum dot product between the input subsequences.
        """
        m, n = len(nums1), len(nums2)

        # Initialize a 1D dp array to store maximum dot products
        dp = [float("-inf")] * (n + 1)

        # Loop through the elements of nums1
        for i in range(1, m + 1):
            # Store the previous diagonal value
            prev_diag = dp[0]
            for j in range(1, n + 1):
                # Store the current dp value
                temp = dp[j]

                # Caclulate the maximum dot product at dp[j]
                dp[j] = max(
                    # Include current elements
                    prev_diag + nums1[i - 1] * nums2[j - 1],
                    # Exclude current element from nums2
                    dp[j - 1],
                    # Exclude current element from nums1
                    dp[j],
                    # Start a new subsequence
                    nums1[i - 1] * nums2[j - 1],
                )

                # Update the previous diagonal value for the next iteration
                prev_diag = temp

        return dp[n]
