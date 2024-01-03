# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/


class Solution:
    """2610. Convert an Array Into a 2D Array With Conditions

    You are given an integer array `nums`. You need to create a 2D array from `nums`
    satisfying the following conditions:

    * The 2D array should contain **only** the elements of the array `nums`.

    * Each row in the 2D array contains **distinct** integers.

    * The number of rows in the 2D array should be **minimal**.

    Return *the resulting array*. If there are multiple answers, return any of them.

    **Note** that the 2D array can have a different number of elements on each row.
    """

    def find_matrix(self, nums: list[int]) -> list[list[int]]:
        # Create a frequency array to keep track of the count of each element
        freq = [0] * (len(nums) + 1)

        # Initialize the result matrix
        ans = []

        # Iterate through each element in the input array
        for c in nums:
            # Check if the current frequency of the element is greater than or equal to
            # the number of rows in the result matrix.
            if freq[c] >= len(ans):
                # If so, add a new row to the result matrix
                ans.append([])

            # Add the current element to the appropriate row in the result matrix
            ans[freq[c]].append(c)

            # Update the frequency count of the current element
            freq[c] += 1

        # Return the resulting matrix
        return ans

    findMatrix = find_matrix
