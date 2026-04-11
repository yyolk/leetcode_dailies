# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii

class Solution:
    """3741. Minimum Distance Between Three Equal Elements II

    You are given an integer array nums. A tuple (i, j, k) of 3 distinct indices is
    good if nums[i] == nums[j] == nums[k]. The distance of a good tuple is
    abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value
    of x. Return an integer denoting the minimum possible distance of a good tuple.
    If no good tuples exist, return -1.
    """
    def minimum_distance(self, nums: list[int]) -> int:
        # Group indices by value using dict of lists
        pos = {}
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            pos[num].append(i)
        
        min_span = float("inf")
        for positions in pos.values():
            m = len(positions)
            if m < 3:
                continue
            # Minimal max-min for any three equal elements occurs among
            # three consecutive positions in the sorted list
            for j in range(m - 2):
                span = positions[j + 2] - positions[j]
                if span < min_span:
                    min_span = span
        
        if min_span == float("inf"):
            return -1
        # For sorted i < j < k the tuple distance simplifies to 2 * (k - i)
        return 2 * min_span

    minimumDistance = minimum_distance