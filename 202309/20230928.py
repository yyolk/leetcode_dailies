# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    """905. Sort Array By Parity

    Given an integer array `nums`, move all the even integers at the beginning of the array
    followed by all the odd integers.

    Return ***any array** that satisfies this condition*.
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Sorts an array with even integers before odd integers

        Proposed solution using two list and concatenation.
        One list for odds, one for evens.

        Args:
            nums (List of int): input nums to sort

        Returns:
            List of int: sorted input with even numbers followed by odd
        """
        evens = []
        odds = []

        # Insert evens and odds into their respective lists
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        # Concatenate the lists, it's now sorted with evens on left, odds on right
        return evens + odds
