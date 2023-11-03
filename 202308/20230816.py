# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque


class Solution:
    """239. Sliding Window Maximum

    You are given an array of integers `nums`, there is a sliding window of size `k`
    which is moving from the very left of the array to the very right. You can only see
    the `k` numbers in the window. Each time the sliding window moves right by one
    position.

    Return *the max sliding window*.
    """

    def max_sliding_window(self, nums: list[int], k: int) -> list[int]:
        """
        Finds the maximum element in a sliding window of size 'k' as it moves from the
        left to the right of an array of integers.

        Args:
            nums: The input array of integers.
            k: The size of the sliding window.

        Returns:
            A list of maximum elements for each position of the sliding window.

        Example:
            >>> nums = [1, 3, -1, -3, 5, 3, 6, 7]
            >>> k = 3
            >>> result = maxSlidingWindow(nums, k)
            >>> print(result)
            [3, 3, 5, 5, 6, 7]
        """
        if not nums:
            return []

        result = []
        max_deque = deque()

        for i in range(len(nums)):
            # Remove elements that are out of the current window from the front.
            while max_deque and max_deque[0] < i - k + 1:
                max_deque.popleft()

            # Remove elements that are smaller than the current element from the back.
            while max_deque and nums[max_deque[-1]] < nums[i]:
                max_deque.pop()

            # Add the current element's index to the the deque.
            max_deque.append(i)

            # Add the maximum element to the result when the window is of the size k.
            if i >= k - 1:
                result.append(nums[max_deque[0]])

        return result

    maxSlidingWindow = max_sliding_window
