# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
from collections import deque


class Solution:
    """2940. Find Building Where Alice and Bob Can Meet

    You are given a **0-indexed** array `heights` of positive integers, where
    `heights[i]` represents the height of the `ith` building.

    If a person is in building `i`, they can move to any other building `j` if and only
    if `i < j` and `heights[i] < heights[j]`.

    You are also given another array `queries` where `queries[i] = [ai, bi]`. On the
    `ith` query, Alice is in building `ai` while Bob is in building `bi`.

    Return *an array* `ans` *where* `ans[i]` *is **the index of the leftmost building**
    where Alice and Bob can meet on the* `ith` *query*. *If Alice and Bob cannot move to
    a common building on query* `i`, *set* `ans[i]` *to* `-1`."""

    def leftmost_building_queries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        # Initialize result list with -1 for all queries
        result_for_queries = [-1] * len(queries)
        
        # List to hold queries that need further processing
        queries_needing_processing = []
        
        # Process each query
        for query_index, query in enumerate(queries):
            alice_position, bob_position = sorted(query)
            
            # Check if Alice and Bob are at the same building or if Bob can see Alice directly
            if alice_position == bob_position or heights[alice_position] < heights[bob_position]:
                result_for_queries[query_index] = bob_position
            else:
                # Add to list for further processing if they can't meet directly
                queries_needing_processing.append((alice_position, bob_position, query_index))

        # Start from the rightmost building
        current_building_index = len(heights) - 1
        
        # Use a deque for monotonic stack to keep track of buildings where meeting could occur
        monotonic_stack = deque()

        # Process queries by sorting based on Bob's position (b) in descending order
        for alice_position, bob_position, query_index in sorted(queries_needing_processing, key=lambda x: x[1], reverse=True):
            # Move left through buildings until we pass Bob's position
            while current_building_index > bob_position:
                # Remove buildings from stack if they are shorter than the current one
                while monotonic_stack and heights[monotonic_stack[0]] < heights[current_building_index]:
                    monotonic_stack.popleft()
                # Add current building to stack
                monotonic_stack.appendleft(current_building_index)
                current_building_index -= 1
            
            # Find the leftmost building where Alice can see or meet with Bob
            building_index = bisect_right(monotonic_stack, heights[alice_position], key=lambda x: heights[x])
            
            # Update result if a meeting point is found, otherwise keep -1
            result_for_queries[query_index] = -1 if building_index == len(monotonic_stack) else monotonic_stack[building_index]

        return result_for_queries

    leftmostBuildingQueries = leftmost_building_queries
