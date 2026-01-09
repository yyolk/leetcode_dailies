# https://leetcode.com/problems/max-dot-product-of-two-subsequences


class Solution:
    """1458. Max Dot Product of Two Subsequences

    Given two arrays nums1 and nums2.

    Return the maximum dot product between non-empty subsequences of nums1
    and nums2 with the same length.

    A subsequence of an array is a new array which is formed from the
    original array by deleting some (can be none) of the characters
    without disturbing the relative positions of the remaining
    characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while
    [1,5,3] is not).
    """
    def max_dot_product(self, nums1: list[int], nums2: list[int]) -> int:
        # Swap if necessary to make nums1 the longer (or equal) array
        # This ensures DP array size is minimized
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        n, m = len(nums1), len(nums2)
        
        # dp[j] = max dot product using first i+1 elements of nums1
        # and first j elements of nums2 (0-based, dp[0] stays -inf)
        dp = [float("-inf")] * (m + 1)
        
        for i in range(n):
            prev_diag = float("-inf")  # dp[i-1][j-1] equivalent
            
            for j in range(m):
                product = nums1[i] * nums2[j]
                
                # Value before updating (skip current nums1[i])
                prev = dp[j + 1]
                
                # Update with:
                # - new length-1 subsequence
                # - extend previous (add to diag)
                # - skip nums1[i]
                # - skip nums2[j] (dp[j] already current row)
                dp[j + 1] = max(
                    product,
                    product + prev_diag,
                    prev,
                    dp[j]
                )
                
                # Prepare diag for next j
                prev_diag = prev
        
        return dp[m]

    maxDotProduct = max_dot_product