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

    def number_of_alternating_groups(self, colors: list[int], k: int) -> int: ...

    numberOfAlternatingGroups = number_of_alternating_groups
