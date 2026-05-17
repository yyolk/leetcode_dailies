# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
import heapq

from math import ceil


class Solution:
    """2530. Maximal Score After Applying K Operations

    You are given a **0\\-indexed** integer array `nums` and an integer `k`. You have a
    **starting score** of `0`.

    In one **operation**:

    1. choose an index `i` such that `0 <= i < nums.length`,

    2. increase your **score** by `nums[i]`, and

    3. replace `nums[i]` with `ceil(nums[i] / 3)`.

    Return *the maximum possible **score** you can attain after applying **exactly***
    `k` *operations*.

    The ceiling function `ceil(val)` is the least integer greater than or equal to
    `val`.

    """

    def max_kelements(self, nums: list[int], k: int) -> int:
        # Convert all numbers to negative for max heap behavior in Python's min heap
        heap = [-num for num in nums]
        heapq.heapify(heap)

        score = 0

        # Perform k operations
        for _ in range(k):
            # Get the largest element (remember, we're working with negatives)
            largest = -heapq.heappop(heap)
            # Add its value to the score
            score += largest

            # Compute new value after operation and push back into heap
            new_value = -ceil(largest / 3)
            heapq.heappush(heap, new_value)

        return score

    maxKelements = max_kelements
