# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

class Solution:
    """1888. Minimum Number of Flips to Make the Binary String Alternating
    
    Return the minimum number of type-2 (flip) operations needed so that s
    becomes alternating (no two adjacent characters are equal), using any
    number of type-1 (rotate left) operations.
    """
    def min_flips(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        # Double the string to handle all possible rotations in linear time
        ss = s + s

        # Target pattern 1: starts with '0' → "010101..."
        # Target pattern 2: starts with '1' → "101010..."
        cost_start_0 = 0
        cost_start_1 = 0

        # Count mismatches for first window of length n
        for i in range(n):
            # For pattern starting with 0
            expected_0 = '0' if i % 2 == 0 else '1'
            if ss[i] != expected_0:
                cost_start_0 += 1

            # For pattern starting with 1
            expected_1 = '1' if i % 2 == 0 else '0'
            if ss[i] != expected_1:
                cost_start_1 += 1

        # Minimum flips needed considering all rotations
        min_flips = min(cost_start_0, cost_start_1)

        # Slide the window over the doubled string
        for i in range(n, 2 * n):
            # Remove leftmost character of previous window
            left = i - n

            # For pattern 010101...
            expected_0_left = '0' if left % 2 == 0 else '1'
            if ss[left] != expected_0_left:
                cost_start_0 -= 1

            expected_0_right = '0' if i % 2 == 0 else '1'
            if ss[i] != expected_0_right:
                cost_start_0 += 1

            # For pattern 101010...
            expected_1_left = '1' if left % 2 == 0 else '0'
            if ss[left] != expected_1_left:
                cost_start_1 -= 1

            expected_1_right = '1' if i % 2 == 0 else '0'
            if ss[i] != expected_1_right:
                cost_start_1 += 1

            # Update minimum after each possible rotation
            min_flips = min(min_flips, cost_start_0, cost_start_1)

        return min_flips

    minFlips = min_flips