# https://leetcode.com/problems/separate-the-digits-in-an-array/


class Solution:
    """2553. Separate the Digits in an Array

    Given an array of positive integers nums, return an array answer that
    consists of the digits of each integer in nums after separating them in
    the same order they appear in nums.
    To separate the digits of an integer is to get all the digits it has in
    the same order.
    For example, for the integer 10921, the separation of its digits is
    [1,0,9,2,1].
    """

    def separate_digits(self, nums: list[int]) -> list[int]:
        # flatten all digits from each num (left-to-right order) into one list
        return [int(digit) for num in nums for digit in str(num)]

    separateDigits = separate_digits
