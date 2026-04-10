# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i

class Solution:
    """3740. Minimum Distance Between Three Equal Elements I
    
    You are given an integer array nums. A tuple (i, j, k) of 3 distinct
    indices is good if nums[i] == nums[j] == nums[k]. The distance of a good
    tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the
    absolute value of x. Return an integer denoting the minimum possible
    distance of a good tuple. If no good tuples exist, return -1.
    """
    def minimum_distance(self, nums: list[int]) -> int:
        # Map each number to list of its indices (positions appended in order)
        positions = {}
        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)
        
        # Track the minimal index span covering any 3 occurrences
        # (distance simplifies to 2 * (max_idx - min_idx) for any triple)
        min_span = float("inf")
        for pos in positions.values():
            if len(pos) >= 3:
                for j in range(len(pos) - 2):
                    # Current triple's span: from pos[j] to pos[j + 2]
                    span = pos[j + 2] - pos[j]
                    if span < min_span:
                        min_span = span
        
        return -1 if min_span == float("inf") else 2 * min_span

    minimumDistance = minimum_distance