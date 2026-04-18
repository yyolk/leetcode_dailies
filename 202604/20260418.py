# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution:
    """3783. Mirror Distance of an Integer

    You are given an integer n. Define its mirror distance as
    abs(n - reverse(n)) where reverse(n) is the integer formed by
    reversing the digits of n. Return an integer denoting the mirror
    distance of n. abs(x) denotes the absolute value of x.
    """
    def mirror_distance(self, n: int) -> int:
        # Convert to string for easy digit reversal
        reversed_str = str(n)[::-1]
        # Convert reversed string back to integer (auto-drops leading zeros)
        reversed_n = int(reversed_str)
        # Return absolute difference for mirror distance
        return abs(n - reversed_n)

    mirrorDistance = mirror_distance