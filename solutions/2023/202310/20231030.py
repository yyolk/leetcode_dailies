# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


class Solution:
    """1356. Sort Integers by The Number of 1 Bits

    You are given an integer array `arr`. Sort the integers in the array in ascending
    order by the number of `1`'s in their binary representation and in case of two or
    more integers have the same number of `1`'s you have to sort them in ascending
    order.

    Return *the array after sorting it*.
    """

    def sort_by_bits(self, arr: list[int]) -> list[int]:
        """Sort input array by their binary representation.

        Sorts the array using `list.sort(...)` with the key function counting the
        number of 1s using `int.bit_count(...)`. If two numbers have the same number
        of 1s, we'll sort again by their original value.

                lambda num: (num.bit_count(), num)
                            ^- primary sort   ^
                                              | secondary sort

        Args:
            arr (list of int): Input integer array to sort by binary representation.
        Returns:
            list of int: Resulting, sorted, integer array.
        """
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr

    sortByBits = sort_by_bits
