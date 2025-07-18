# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
import heapq


class Solution:
    """2163. Minimum Difference in Sums After Removal of Elements

    You are given a **0-indexed** integer array `nums` consisting of `3 * n` elements.

    You are allowed to remove any **subsequence** of elements of size **exactly** `n`
    from `nums`. The remaining `2 * n` elements will be divided into two **equal**
    parts:

    * The first `n` elements belonging to the first part and their sum is `sumfirst`.

    * The next `n` elements belonging to the second part and their sum is `sumsecond`.

    The **difference in sums** of the two parts is denoted as `sumfirst - sumsecond`.

    * For example, if `sumfirst = 3` and `sumsecond = 2`, their difference is `1`.

    * Similarly, if `sumfirst = 2` and `sumsecond = 3`, their difference is `-1`.

    Return *the **minimum difference** possible between the sums of the two parts after
    the removal of* `n` *elements*."""

    def minimum_difference(self, nums: list[int]) -> int:
        # Calculate n as one-third of the length of nums
        n = len(nums) // 3
        # Comment for the left part: using a max-heap (simulated with negatives in min-heap) to maintain the smallest n elements for the left side
        # Left: max-heap (using negatives) to maintain smallest n elements
        # Initialize an empty list for the left heap
        left_heap = []
        # Initialize the sum for the left part to 0
        left_sum = 0
        # Loop to add the first n elements to the left heap and sum
        for i in range(n):
            # Push the negative of nums[i] to simulate max-heap
            heapq.heappush(left_heap, -nums[i])
            # Add nums[i] to left_sum
            left_sum += nums[i]
        # Initialize a list to store left sums, size n+1, filled with 0
        left_sums = [0] * (n + 1)
        # Set the initial left sum (sum of smallest n in first n elements)
        left_sums[0] = left_sum
        # Loop to process the next n elements for the left part
        for i in range(n):
            # Push the negative of the next element to the heap
            heapq.heappush(left_heap, -nums[n + i])
            # Add the next element to left_sum
            left_sum += nums[n + i]
            # Pop the largest element (smallest negative) and negate back to positive
            popped = -heapq.heappop(left_heap)
            # Subtract the popped (largest) from left_sum to keep sum of smallest n
            left_sum -= popped
            # Store the updated sum in left_sums
            left_sums[i + 1] = left_sum
        
        # Comment for the right part: using a min-heap to maintain the largest n elements for the right side
        # Right: min-heap to maintain largest n elements
        # Initialize an empty list for the right heap
        right_heap = []
        # Initialize the sum for the right part to 0
        right_sum = 0
        # Loop to add the last n elements to the right heap and sum, in reverse order
        for i in range(3 * n - 1, 2 * n - 1, -1):
            # Push nums[i] to the min-heap
            heapq.heappush(right_heap, nums[i])
            # Add nums[i] to right_sum
            right_sum += nums[i]
        # Initialize a list to store right sums, size n+1, filled with 0
        right_sums = [0] * (n + 1)
        # Set the initial right sum (sum of largest n in last n elements)
        right_sums[0] = right_sum
        # Loop to process the previous n elements for the right part
        for i in range(n):
            # Calculate the number to add, moving backwards from the middle
            add_num = nums[2 * n - 1 - i]
            # Push the add_num to the min-heap
            heapq.heappush(right_heap, add_num)
            # Add add_num to right_sum
            right_sum += add_num
            # Pop the smallest element from the heap
            popped = heapq.heappop(right_heap)
            # Subtract the popped (smallest) from right_sum to keep sum of largest n
            right_sum -= popped
            # Store the updated sum in right_sums
            right_sums[i + 1] = right_sum
        
        # Initialize answer to positive infinity
        ans = float('inf')
        # Loop over possible i to find the minimum difference
        for i in range(n + 1):
            # Update ans with the minimum of current ans and the difference left_sums[i] - right_sums[n - i]
            ans = min(ans, left_sums[i] - right_sums[n - i])
        # Return the computed minimum difference
        return ans

    minimumDifference = minimum_difference
