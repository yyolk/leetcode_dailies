# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq


class Solution:
    """215. Kth Largest Element in an Array

    Given an integer array `nums` and an integer `k`, return *the* `kth` *largest
    element in the array*.

    Note that it is the `kth` largest element in the sorted order, not the `kth`
    distinct element.

    Can you solve it without sorting?
    """

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        """Finds the kth largest element.

        Args:
            nums: Input array of nums to search.
            k: Input target as kth largest element.

        Returns:
            The kth largest element in the input array.
        """
        # Create a min-heap to store the k largest elements.
        min_heap = []

        # Push the first k elements into the min-heap.
        for num in nums[:k]:
            heapq.heappush(min_heap, num)

        # Iterate through the remaining elements in the array.
        for num in nums[k:]:
            # If the current element is greater than the smallest element in the min-heap,
            # replace the smallest element with the current element.
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # The min-heap now contains the k largest elements, and the smallest element
        # in the min-heap is the kth largest element in the array.
        return min_heap[0]

    findKthLargest = find_kth_largest
