# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/


class Solution:
    """3480. Maximize Subarrays After Removing One Conflicting Pair

    You are given an integer `n` which represents an array `nums` containing the numbers
    from 1 to `n` in order. Additionally, you are given a 2D array `conflicting_pairs`,
    where `conflicting_pairs[i] = [a, b]` indicates that `a` and `b` form a conflicting
    pair.

    Remove **exactly** one element from `conflicting_pairs`. Afterward, count the number
    of non-empty subarrays of `nums` which do not contain both `a` and `b` for any
    remaining conflicting pair `[a, b]`.

    Return the **maximum** number of subarrays possible after removing **exactly** one
    conflicting pair."""

    def max_subarrays(self, n: int, conflicting_pairs: list[list[int]]) -> int:
        # Initialize counter for valid subarrays
        valid_subarrays = 0
        # Track the maximum left boundary of conflicting elements
        max_left = 0
        # Track the second maximum left boundary for gain calculation
        second_max_left = 0
        # Store potential gain in subarrays for each position when chosen for removal
        gains = [0] * (n + 1)
        # Create adjacency list to store conflicts for each right element
        conflicts = [[] for _ in range(n + 1)]

        # Build conflict graph: for each pair [a,b], store min(a,b) at max(a,b)
        for a, b in conflicting_pairs:
            conflicts[max(a, b)].append(min(a, b))

        # Iterate through each possible right boundary
        for right in range(1, n + 1):
            # Update max_left and second_max_left for current right boundary
            for left in conflicts[right]:
                if left > max_left:
                    # Update second_max_left before updating max_left
                    second_max_left = max_left
                    # Set new max_left
                    max_left = left
                elif left > second_max_left:
                    # Update second_max_left if left is between max_left and current second_max_left
                    second_max_left = left
            # Add valid subarrays ending at right (from max_left to right)
            valid_subarrays += right - max_left
            # Calculate potential gain if max_left element is removed
            gains[max_left] += max_left - second_max_left

        # Return total valid subarrays plus maximum gain from removing one conflict
        return valid_subarrays + max(gains)

    maxSubarrays = max_subarrays
