# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    """1295. Find Numbers with Even Number of Digits

    Given an array `nums` of integers, return how many of them contain an **even
    number** of digits."""

    def find_numbers(self, nums: list[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)

    findNumbers = find_numbers
