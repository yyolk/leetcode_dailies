# https://leetcode.com/problems/132-pattern/


class Solution:
    """456. 132 Pattern

    Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three
    integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k]
    < nums[j]`.

    Return `true` *if there is a **132 pattern** in* `nums`*, otherwise, return* `false`*.*
    """

    def find132pattern(self, nums: List[int]) -> bool:
        """Finds if theres a pattern of 132 in the provided input

        Proposed solution

        Args:
            nums (List of int): the input nums to search for 132 pattern

        Returns:
            bool: whether the input nums contains a 132 pattern in the sequence
        """
        n = len(nums)
        # This will always be false
        if n < 3:
            return False

        # Create a stack to keep track of the potential '2' in the pattern
        stack = []

        # Initialize the '3' (max) to negative infinity
        max_val = float("-inf")

        # Iterate in the reverse order
        for i in range(n - 1, -1, -1):
            # If we find a number smaller than the current max, it's a potential '1'
            if nums[i] < max_val:
                return True

            # Pop elements from the stack as long as they are smaller than the
            # current number
            while stack and nums[i] > stack[-1]:
                max_val = stack.pop()

            # Push the current number onto the stack
            stack.append(nums[i])

        # No 132 pattern was found
        return False
