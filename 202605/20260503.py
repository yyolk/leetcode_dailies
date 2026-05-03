# https://leetcode.com/problems/rotate-string

class Solution:
    """796. Rotate String
    
    Given two strings s and goal, return true if and only if s can become goal
    after some number of shifts on s. A shift on s consists of moving the
    leftmost character of s to the rightmost position. For example, if s =
    "abcde", then it will be "bcdea" after one shift.
    """
    def rotate_string(self, s: str, goal: str) -> bool:
        # Early return if lengths differ - impossible to rotate to different length
        if len(s) != len(goal):
            return False
        # goal is a rotation of s iff it appears in s+s
        # All possible rotations are substrings of s concatenated with itself
        return goal in s + s

    rotateString = rotate_string