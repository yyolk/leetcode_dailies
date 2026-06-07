# https://leetcode.com/problems/rotate-string/


class Solution:
    """796. Rotate String

    Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become*
    `goal` *after some number of **shifts** on* `s`.

    A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost
    position.

    * For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

    """

    def rotate_string(self, s: str, goal: str) -> bool:
        # Check if lengths are different, if so, they can't be rotations of each other
        if len(s) != len(goal):
            return False

        # Concatenate s with itself. If goal is a rotation, it must be a substring of this.
        s_double = s + s

        # Check if goal is a substring of s+s
        return goal in s_double

    rotateString = rotate_string
