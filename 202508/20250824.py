# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


class Solution:
    """1493. Longest Subarray of 1's After Deleting One Element

    Given a binary array `nums`, you should delete one element from it.

    Return *the size of the longest non-empty subarray containing only* `1`*'s in the
    resulting array*. Return `0` if there is no such subarray."""

    def longest_subarray(self, nums: list[int]) -> int:
        # Get the length of the input array
        n = len(nums)
        # Handle empty array case
        if n == 0:
            return 0

        # Initialize lists to store lengths of 1's streaks and gaps of 0's between them
        streaks = []
        gap_sizes = []
        # Index to traverse the array
        i = 0

        # Skip any initial 0's
        while i < n and nums[i] == 0:
            i += 1
        # If entire array is 0's, return 0
        if i == n:
            return 0

        # Find the first streak of 1's
        start = i
        while i < n and nums[i] == 1:
            i += 1
        # Append the length of the first streak
        streaks.append(i - start)

        # Process the rest of the array for additional streaks and gaps
        while i < n:
            # Count the gap of consecutive 0's
            gap_start = i
            while i < n and nums[i] == 0:
                i += 1
            # If reached end after trailing 0's, break
            if i == n:
                break
            # Calculate and append the gap size
            gap = i - gap_start
            gap_sizes.append(gap)

            # Find the next streak of 1's
            start = i
            while i < n and nums[i] == 1:
                i += 1
            # Append the length of this streak
            streaks.append(i - start)

        # Calculate the maximum streak length
        max_streak = max(streaks)
        # Calculate total number of 1's
        total_ones = sum(streaks)

        # If the array is all 1's, must delete one 1
        if total_ones == n:
            return n - 1

        # Initialize answer with the max streak (achievable since 0's exist to delete)
        ans = max_streak
        # Check for possible merges where gap is exactly 1
        for j in range(len(gap_sizes)):
            if gap_sizes[j] == 1:
                # Update answer with merged length if larger
                ans = max(ans, streaks[j] + streaks[j + 1])

        return ans

    longestSubarray = longest_subarray
