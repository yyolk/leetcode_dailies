# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq


class KthLargest:
    """789. Kth Largest Element in a Stream

    Design a class to find the `kth` largest element in a stream. Note that it is the
    `kth` largest element in the sorted order, not the `kth` distinct element.

    Implement `KthLargest` class:

    * `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and
    the stream of integers `nums`.

    * `int add(int val)` Appends the integer `val` to the stream and returns the element
    representing the `kth` largest element in the stream.

    Your KthLargest object will be instantiated and called as such:

        obj = KthLargest(k, nums)
        param_1 = obj.add(val)
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Maintain the heap size to be exactly k by popping smallest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.heap, val)
        # If the heap size exceeds k, pop the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The root of the heap is the kth largest element
        return self.heap[0]
