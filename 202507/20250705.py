# https://leetcode.com/problems/find-lucky-integer-in-an-array/


class Solution:
    """1394. Find Lucky Integer in an Array

    Given an array of integers `arr`, a **lucky integer** is an integer that has a
    frequency in the array equal to its value.

    Return *the largest **lucky integer** in the array*. If there is no **lucky
    integer** return `-1`."""

    def find_lucky(self, arr: list[int]) -> int:
        # Count frequency of each number using a dictionary
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Find lucky numbers where frequency equals value
        lucky = -1
        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)
        
        return lucky

    findLucky = find_lucky
