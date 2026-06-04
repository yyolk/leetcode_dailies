# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/


class Solution:
    """3751. Total Waviness of Numbers in Range I

    You are given two integers num1 and num2 representing an inclusive range
    [num1, num2]. The waviness of a number is defined as the total count of its
    peaks and valleys: A digit is a peak if it is strictly greater than both of
    its immediate neighbors. A digit is a valley if it is strictly less than
    both of its immediate neighbors. The first and last digits of a number
    cannot be peaks or valleys. Any number with fewer than 3 digits has a
    waviness of 0. Return the total sum of waviness for all numbers in the
    range [num1, num2]."""

    def total_waviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            # convert to string for digit access
            s = str(num)
            if len(s) < 3:
                continue  # waviness 0
            for i in range(1, len(s) - 1):
                # check internal digit (char comparison valid for '0'-'9')
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (
                    s[i] < s[i - 1] and s[i] < s[i + 1]
                ):
                    total += 1
        return total

    totalWaviness = total_waviness
