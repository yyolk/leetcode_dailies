# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
import heapq


class Solution:
    """2593. Find Score of an Array After Marking All Elements

    You are given an array `nums` consisting of positive integers.

    Starting with `score = 0`, apply the following algorithm:

    * Choose the smallest integer of the array that is not marked. If there is a tie,
    choose the one with the smallest index.

    * Add the value of the chosen integer to `score`.

    * Mark **the chosen element and its two adjacent elements if they exist**.

    * Repeat until all the array elements are marked.

    Return *the score you get after applying the above algorithm*."""

    def find_score(self, nums: list[int]) -> int:
        # Use a min heap to always get the smallest unmarked number
        # Each element in the heap is a tuple (value, index)
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        
        score = 0
        marked = [False] * len(nums)
        
        while heap:
            val, index = heapq.heappop(heap)
            if not marked[index]:  # If the number hasn't been marked
                score += val
                marked[index] = True
                # Mark the two adjacent numbers if they exist
                if index > 0:
                    marked[index - 1] = True
                if index < len(nums) - 1:
                    marked[index + 1] = True
        
        return score

    findScore = find_score
