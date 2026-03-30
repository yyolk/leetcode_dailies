# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii

class Solution:
    """2840. Check if Strings Can be Made Equal With Operations II
    
    You are given two strings s1 and s2, both of length n, consisting of lowercase
    English letters.
    You can apply the following operation on any of the two strings any number of
    times:
    Choose any two indices i and j such that i < j and the difference j - i is
    even, then swap the two characters at those indices in the string.
    Return true if you can make the strings s1 and s2 equal, and false otherwise.
    """
    def check_strings(self, s1: str, s2: str) -> bool:
        # even indices (0, 2, 4, ...) can be freely rearranged in each string
        # because any pair has even distance
        even1 = sorted(s1[::2])
        even2 = sorted(s2[::2])
        # odd indices (1, 3, 5, ...) can be freely rearranged independently
        odd1 = sorted(s1[1::2])
        odd2 = sorted(s2[1::2])
        # multisets of even positions must match between s1 and s2;
        # same requirement holds for odd positions
        return even1 == even2 and odd1 == odd2

    checkStrings = check_strings