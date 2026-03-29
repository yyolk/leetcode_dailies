# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i

class Solution:
    """2839. Check if Strings Can be Made Equal With Operations I
    
    You are given two strings s1 and s2, both of length 4, consisting of
    lowercase English letters. You can apply the following operation on any
    of the two strings any number of times: Choose any two indices i and j
    such that j - i = 2, then swap the two characters at those indices in
    the string. Return true if you can make the strings s1 and s2 equal,
    and false otherwise.
    """
    def can_be_equal(self, s1: str, s2: str) -> bool:
        # s1[::2] selects chars at even indices 0/2; s1[1::2] at odd 1/3
        # these pairs can be swapped independently in either string
        return (sorted(s1[::2]) == sorted(s2[::2]) and
                sorted(s1[1::2]) == sorted(s2[1::2]))

    canBeEqual = can_be_equal