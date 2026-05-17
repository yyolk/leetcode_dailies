# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
from collections import defaultdict


class Solution:
    """2342. Max Sum of a Pair With Equal Sum of Digits

    You are given a **0-indexed** array `nums` consisting of **positive** integers. You
    can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the
    number `nums[i]` is equal to that of `nums[j]`.

    Return *the **maximum** value of* `nums[i] + nums[j]` *that you can obtain over all
    possible indices* `i` *and* `j` *that satisfy the conditions.*"""

    def maximum_sum(self, nums: list[int]) -> int:
        # Function to calculate the sum of digits of a number
        def sum_of_digits(num: int) -> int:
            return sum(int(digit) for digit in str(num))

        # Dictionary to store the maximum two numbers for each digit sum
        digit_sum_map = defaultdict(list)

        # Iterate through the numbers and populate the dictionary
        for num in nums:
            digit_sum = sum_of_digits(num)
            digit_sum_map[digit_sum].append(num)

        # Initialize with -1 to handle cases where no valid pair is found
        max_sum = -1

        # Iterate through the dictionary to find the maximum sum of two numbers
        for key in digit_sum_map:
            if len(digit_sum_map[key]) >= 2:
                # Sort the list in descending order and take the top two elements
                sorted_nums = sorted(digit_sum_map[key], reverse=True)
                current_sum = sorted_nums[0] + sorted_nums[1]
                if current_sum > max_sum:
                    max_sum = current_sum

        return max_sum

    maximumSum = maximum_sum
