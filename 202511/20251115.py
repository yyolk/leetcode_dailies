# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/


class Solution:
    """3234. Count the Number of Substrings With Dominant Ones

    You are given a binary string s.

    Return the number of substrings with dominant ones.

    A string has dominant ones if the number of ones in the string is greater
    than or equal to the square of the number of zeros in the string.
    """
    def number_of_substrings(self, s: str) -> int:
        # Length of the string
        n = len(s)
        # List of positions where '0' appears
        pos = [i for i in range(n) if s[i] == '0']
        # Number of '0's
        k = len(pos)
        # Add sentinels for boundary handling
        pos = [-1] + pos + [n]
        # Initialize answer
        ans = 0
        # Handle z=0: all substrings within each group of consecutive '1's
        for i in range(k + 1):
            # Length of '1's group between pos[i] and pos[i+1]
            L = pos[i + 1] - pos[i] - 1
            # Add number of substrings in this group
            ans += L * (L + 1) // 2
        # Compute max possible z where z*(z+1) <= n
        import math
        max_z = int((-1 + math.sqrt(1 + 4 * n)) / 2)
        # For each possible z from 1 to max_z
        for z in range(1, max_z + 1):
            # Minimum length required for this z
            m = z * z + z
            # d = m - 1 for end - start >= d
            d = m - 1
            # For each starting zero index jj
            for jj in range(1, k - z + 2):
                # Position of first zero in the group
                first = pos[jj]
                # Position of last zero in the group
                last = pos[jj + z - 1]
                # Minimum start position
                left_b = pos[jj - 1] + 1
                # Maximum end position
                right_b = pos[jj + z] - 1
                # Maximum start position (at first zero)
                max_s = first
                # Minimum end position (at last zero)
                min_e = last
                # Split point where threshold changes from constant to variable
                split_p = min_e - d
                # Constant number of ends when threshold is min_e
                const_n = max(0, right_b - min_e + 1)
                # Fixed contribution: s from left_b to min(max_s, split_p)
                left_f = left_b
                right_f = min(max_s, split_p)
                contrib_f = 0
                if left_f <= right_f:
                    # Number of starts in fixed range
                    num_f = right_f - left_f + 1
                    # Contribution: num starts * const ends
                    contrib_f = num_f * const_n
                # Variable contribution: s from max(left_b, split_p+1) to max_s
                left_v = max(left_b, split_p + 1)
                right_v = max_s
                contrib_v = 0
                if left_v <= right_v:
                    # c for var_num(s) = max(0, c - s)
                    c = right_b - d + 1
                    # Last s where c - s >= 0
                    right_pos = min(right_v, c)
                    if left_v <= right_pos:
                        # Number of terms in sum
                        num_v = right_pos - left_v + 1
                        # Sum of s from left_v to right_pos
                        sum_s_v = num_v * (left_v + right_pos) // 2
                        # Sum of (c - s) = num * c - sum s
                        contrib_v = num_v * c - sum_s_v
                # Add contributions to answer
                ans += contrib_f + contrib_v
        return ans

    numberOfSubstrings = number_of_substrings