# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


class Solution:
    """1007. Minimum Domino Rotations For Equal Row

    In a row of dominoes, `tops[i]` and `bottoms[i]` represent the top and bottom halves
    of the `ith` domino. (A domino is a tile with two numbers from 1 to 6 - one on each
    half of the tile.)

    We may rotate the `ith` domino, so that `tops[i]` and `bottoms[i]` swap values.

    Return the minimum number of rotations so that all the values in `tops` are the
    same, or all the values in `bottoms` are the same.

    If it cannot be done, return `-1`."""

    def min_domino_rotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        # Initialize frequency counters for values 1 to 6 (index 0 is unused)
        count_tops = [0] * 7
        count_bottoms = [0] * 7

        # Count occurrences of each value in tops and bottoms
        for i in range(n):
            count_tops[tops[i]] += 1
            count_bottoms[bottoms[i]] += 1

        # Find possible target values by intersecting {tops[i], bottoms[i]} for all i
        candidates = set(
            range(1, 7)
        )  # Start with all possible values: {1, 2, 3, 4, 5, 6}
        for i in range(n):
            candidates &= {tops[i], bottoms[i]}
            if not candidates:
                break  # Early exit if no possible targets remain

        # If no value can be made uniform across tops or bottoms, return -1
        if not candidates:
            return -1

        # Find the maximum count achievable for any candidate value
        max_count = 0
        for x in candidates:
            max_count = max(max_count, count_tops[x], count_bottoms[x])

        # Minimum rotations is the number of dominoes minus the maximum count
        return n - max_count

    minDominoRotations = min_domino_rotations
