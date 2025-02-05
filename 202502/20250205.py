# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    """1790. Check if One String Swap Can Make Strings Equal

    You are given two strings `s1` and `s2` of equal length. A **string swap** is an
    operation where you choose two indices in a string (not necessarily different) and
    swap the characters at these indices.

    Return `true` *if it is possible to make both strings equal by performing **at most
    one string swap** on **exactly one** of the strings.* Otherwise, return `false`."""

    def are_almost_equal(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, return True
        if s1 == s2:
            return True
        
        # Find the indices where the characters differ
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        # If there are more than two differences, return False
        if len(diff_indices) != 2:
            return False
        
        # Check if swapping the characters at the two indices makes the strings equal
        i, j = diff_indices
        return s1[i] == s2[j] and s1[j] == s2[i]

    areAlmostEqual = are_almost_equal
