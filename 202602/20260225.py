# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits


class Solution:
    """1356. Sort Integers by The Number of 1 Bits
    
    You are given an integer array arr. Sort the integers in the array
    in ascending order by the number of 1's in their binary representation
    and in case of two or more integers have the same number of 1's you
    have to sort them in ascending order.
    
    Return the array after sorting it.
    """
    def sort_by_bits(self, arr: list[int]) -> list[int]:
        # Sort by (number of 1-bits, value) tuple for primary then secondary key
        # bin(x).count("1") computes popcount; stable sort not needed due to tuple
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))

    sortByBits = sort_by_bits