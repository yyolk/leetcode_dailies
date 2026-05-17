# https://leetcode.com/problems/alternating-groups-ii/


class Solution:
    """3208. Alternating Groups II

    There is a circle of red and blue tiles. You are given an array of integers `colors`
    and an integer `k`. The color of tile `i` is represented by `colors[i]`:

    * `colors[i] == 0` means that tile `i` is **red**.

    * `colors[i] == 1` means that tile `i` is **blue**.

    An **alternating** group is every `k` contiguous tiles in the circle with
    **alternating** colors (each tile in the group except the first and last one has a
    different color from its **left** and **right** tiles).

    Return the number of **alternating** groups.

    **Note** that since `colors` represents a **circle**, the **first** and the **last**
    tiles are considered to be next to each other."""

    def number_of_alternating_groups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        # Step 1: Extend the array to handle circularity
        extended_colors = colors + colors[: k - 1]

        # Step 2: Create an array to track alternating pairs
        diff = [
            1 if extended_colors[i] != extended_colors[i + 1] else 0
            for i in range(len(extended_colors) - 1)
        ]

        # Step 3: Initialize the sum for the first window of size k-1
        current_sum = sum(diff[: k - 1])
        count = 0

        # Check the first group
        if current_sum == k - 1:
            count += 1

        # Step 4: Slide the window across all n starting positions
        for i in range(1, n):
            # Update window sum: subtract the leftmost, add the rightmost
            current_sum = current_sum - diff[i - 1] + diff[i + k - 2]
            if current_sum == k - 1:
                count += 1

        return count

    numberOfAlternatingGroups = number_of_alternating_groups
