# https://leetcode.com/problems/rotated-digits/


class Solution:
    """788. Rotated Digits
    
    An integer x is a good if after rotating each digit individually by 180
    degrees, we get a valid number that is different from x. Each digit must be
    rotated - we cannot choose to leave it alone.
    
    A number is valid if each digit remains a digit after rotation. For example:
    0, 1, and 8 rotate to themselves, 2 and 5 rotate to each other, 6 and 9
    rotate to each other, and the rest of the numbers do not rotate to any
    other number and become invalid.
    
    Given an integer n, return the number of good integers in the range [1, n].
    """
    def rotated_digits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            # convert to string for digit access
            s = str(i)
            # skip if any invalid digit (cannot rotate to valid digit)
            if any(d in "347" for d in s):
                continue
            # must contain at least one changing digit to differ after rotation
            if any(d in "2569" for d in s):
                count += 1
        return count

    rotatedDigits = rotated_digits