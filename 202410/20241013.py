# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
import heapq


class Solution:
    """632. Smallest Range Covering Elements from K Lists

    You have `k` lists of sorted integers in **non\\-decreasing order**. Find the
    **smallest** range that includes at least one number from each of the `k` lists.

    We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c`
    **or** `a < c` if `b - a == d - c`.

    """

    def smallest_range(self, nums: list[list[int]]) -> list[int]:
        # Heap to store {value, list_index, value_index}
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)
        
        # To keep track of the maximum value in the current range
        max_val = max(row[0] for row in nums)
        
        # Initial result 
        result = [pq[0][0], max_val]
        
        while pq:
            # Pop the smallest element
            min_val, list_index, value_index = heapq.heappop(pq)
            
            # Check if this range is smaller than our current best
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]
            
            # If we have exhausted a list, we cannot extend our range anymore
            if value_index + 1 == len(nums[list_index]):
                return result
            
            # Push the next number from the same list into the heap
            next_val = nums[list_index][value_index + 1]
            heapq.heappush(pq, (next_val, list_index, value_index + 1))
            # Update max_val if necessary
            if next_val > max_val:
                max_val = next_val
        
        # This line should not be reached if there's a valid solution
        return result

    smallestRange = smallest_range
