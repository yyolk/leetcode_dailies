# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/


class Solution:
    """3542. Minimum Operations to Convert All Elements to Zero

    You are given an array nums of size n, consisting of non-negative integers.
    Your task is to apply some (possibly zero) operations on the array so that
    all elements become 0.

    In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n)
    and set all occurrences of the minimum non-negative integer in that
    subarray to 0.

    Return the minimum number of operations required to make all elements in
    the array 0.
    """
    def min_operations(self, nums: list[int]) -> int:
        # Initialize the operation count
        ans = 0
        # Use a list as stack, starting with 0 to handle minima
        stack = [0]
        # Iterate through each number in the array
        for num in nums:
            # Pop from stack while top is greater than current num
            while stack and stack[-1] > num:
                stack.pop()
            # If stack is empty or top is less than num, it's a new operation
            if not stack or stack[-1] < num:
                ans += 1
                # Push the num onto the stack
                stack.append(num)
        return ans

    minOperations = min_operations