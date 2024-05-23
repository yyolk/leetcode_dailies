# https://leetcode.com/problems/the-number-of-beautiful-subsets/
from collections import defaultdict


class Solution:
    """2597. The Number of Beautiful Subsets

    You are given an array `nums` of positive integers and a **positive** integer `k`.

    A subset of `nums` is **beautiful** if it does not contain two integers with an
    absolute difference equal to `k`.

    Return *the number of **non-empty beautiful** subsets of the array* `nums`.

    A **subset** of `nums` is an array that can be obtained by deleting some (possibly
    none) elements from `nums`. Two subsets are different if and only if the chosen
    indices to delete are different.

    """

    def beautiful_subsets(self, nums: list[int], k: int) -> int:
        # Start with a total count of 1 (empty subset)
        total_count = 1
        frequency_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            remainder = num % difference
            frequency_map[remainder][num] = frequency_map[remainder].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in frequency_map.values():
            n = len(fr)
            curr_count = 1
            next1 = 1
            next2 = 0
            subsets = sorted(fr.items())

            # Calculate counts for each subset starting from the second last
            for i in range(n - 1, -1, -1):
                # Count of subsets skipping the current subset
                skip = next1

                # Count of subsets including the current subset
                take = 2 ** subsets[i][1] - 1

                # If next number has a 'difference', calculate subsets; otherwise, move to next
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == difference:
                    take *= next2
                else:
                    take *= next1

                # Store the current total count for the current subset
                curr_count = skip + take
                next2, next1 = next1, curr_count

            total_count *= curr_count

        # Subtract 1 to exclude the empty subset
        return total_count - 1

    beautifulSubsets = beautiful_subsets
