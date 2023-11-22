# https://leetcode.com/problems/frequency-of-the-most-frequent-element/


class Solution:
    """1838. Frequency of the Most Frequent Element

    The **frequency** of an element is the number of times it occurs in an array.

    You are given an integer array `nums` and an integer `k`. In one operation, you can
    choose an index of `nums` and increment the element at that index by `1`.

    Return *the **maximum possible frequency** of an element after performing **at
    most*** `k` *operations*.
    """

    def max_frequency(self, nums: list[int], k: int) -> int:
        """The maximum possible frequency of an element post, at most, k operations.

        Using a sliding window.

        Args:
            nums: Input list of integer elements.
            k: Max operations to perform.

        Returns:
            Frequency of an element after performing at most k operations.
        """
        # Sort the array in non-decreasing order.
        nums.sort()
        n = len(nums)
        max_freq = 0
        operations = 0
        left = 0

        # Iterate through the sorted list.
        for right in range(n):
            operations += nums[right]

            # While the operations exceed the limit, move the left pointer
            while (right - left + 1) * nums[right] > operations + k:
                operations -= nums[left]
                left += 1

            # Update the maximum frequency.
            max_freq = max(max_freq, right - left + 1)

        # Return the maximum frequency
        return max_freq

    maxFrequency = max_frequency
