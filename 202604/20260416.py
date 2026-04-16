# https://leetcode.com/problems/closest-equal-element-queries

from collections import defaultdict

class Solution:
    """3488. Closest Equal Element Queries
    
    You are given a circular array nums and an array queries.
    For each query i, you have to find the minimum distance between the
    element at index queries[i] and any other index j in the circular
    array, where nums[j] == nums[queries[i]]. If no such index exists,
    the answer for that query should be -1.
    Return an array answer of the same size as queries, where answer[i]
    represents the result for query i.
    """
    def solve_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        # Group indices by value (already sorted as we iterate left to right)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(i)
        
        # Precompute min circular dist for each index (default -1 if unique)
        min_dist = [-1] * n
        for positions in pos.values():
            k = len(positions)
            if k < 2:
                continue
            # For each position, min dist is to its circular neighbors only
            for i in range(k):
                curr = positions[i]
                # Previous and next indices on the circular positions list
                left = positions[(i - 1) % k]
                right = positions[(i + 1) % k]
                # Circular distance to left neighbor
                d_left = min(abs(curr - left), n - abs(curr - left))
                # Circular distance to right neighbor
                d_right = min(abs(curr - right), n - abs(curr - right))
                min_dist[curr] = min(d_left, d_right)
        
        # Build answer directly from precomputed distances
        answer = [min_dist[q] for q in queries]
        return answer

    solveQueries = solve_queries