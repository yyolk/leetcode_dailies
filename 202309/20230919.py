# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    """287. Find the Duplicate Number

    Given an array of integers `nums` containing `n + 1` integers where each integer is in
    the range `[1, n]` inclusive.

    There is only **one repeated number** in `nums`, return *this repeated number*.

    You must solve the problem **without** modifying the array `nums` and uses only constant
    extra space.
    """

    def findDuplicate(self, nums: list[int]) -> int:
        """Finds the duplicate number

        Proposed solution using Floyd's Tortoise and Hare algorithm.
        It can be adapted to find the repeated number in an array.

        Args:
            nums (list of int): the input number array with one duplicate number

        Returns:
            int: the duplicate number in the input array
        """
        # Initialize the tortoise and hare pointers as slow and fast
        slow = nums[0]
        fast = nums[0]

        # Move the slow pointer one step and the fast pointer two steps until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the entrance point of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the repeated number
        return slow
