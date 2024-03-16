# https://leetcode.com/problems/contiguous-array/


class Solution:
    """525. Contiguous Array

    Given a binary array `nums`, return *the maximum length of a contiguous subarray
    with an equal number of* `0` *and* `1`.

    """

    def find_max_length(self, nums: list[int]) -> int:
        # Initialize a dictionary to keep track of the first occurrence of a balance
        # and its corresponding index.
        count = {0: -1}
        # Initialize variables to keep track of the maximum length of a subarray
        # and the current balance.
        max_length = 0
        balance = 0

        # Iterate through the input array and update the balance.
        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            # If the current balance has been seen before, calculate the length of
            # the subarray with the same balance and update the maximum length.
            if balance in count:
                max_length = max(max_length, i - count[balance])
            # If the current balance is encountered for the first time, store its
            # index in the dictionary.
            else:
                count[balance] = i

        return max_length

    findMaxLength = find_max_length
