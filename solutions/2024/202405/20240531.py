# https://leetcode.com/problems/single-number-iii/


class Solution:
    """260. Single Number III

    Given an integer array `nums`, in which exactly two elements appear only once and
    all the other elements appear exactly twice. Find the two elements that appear only
    once. You can return the answer in **any order**.

    You must write an algorithm that runs in linear runtime complexity and uses only
    constant extra space.

    """

    def single_number(self, nums: list[int]) -> list[int]:
        # Step 1: XOR all the numbers to get the XOR of the two unique numbers
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # Step 2: Find a set bit (rightmost set bit) in xor_result
        # This bit will be different in the two unique numbers
        diff_bit = xor_result & -xor_result

        # Step 3: Divide the numbers into two groups based on the diff_bit
        # and XOR the numbers in each group to find the unique numbers
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num

        # Step 4: Return the two unique numbers
        return [num1, num2]

    singleNumber = single_number
