# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

from functools import lru_cache


class Solution:
    """3753. Total Waviness of Numbers in Range II

    You are given two integers num1 and num2 representing an inclusive range
    [num1, num2].
    The waviness of a number is defined as the total count of its peaks and
    valleys:
    * A digit is a peak if it is strictly greater than both of its immediate
    neighbors.
    * A digit is a valley if it is strictly less than both of its immediate
    neighbors.
    * The first and last digits of a number cannot be peaks or valleys.
    * Any number with fewer than 3 digits has a waviness of 0.
    Return the total sum of waviness for all numbers in the range [num1, num2].
    """

    def total_waviness(self, num1: int, num2: int) -> int:
        def sum_up_to(num: int) -> int:
            # compute total waviness for all numbers from 0 to num (inclusive)
            if num < 0:
                return 0
            digits = [int(c) for c in str(num)]
            L = len(digits)

            @lru_cache(None)
            def dp(
                pos: int, tight: int, pprev: int, prev: int, started: int
            ) -> tuple[int, int]:
                # dp returns (number_count, waviness_sum) from this state
                if pos == L:
                    # end of digits: valid number built, waviness already accounted
                    return 1, 0

                ans_c = 0
                ans_s = 0
                up = digits[pos] if tight else 9

                for d in range(up + 1):
                    # determine new tight flag
                    ntight = 1 if tight and d == up else 0

                    if started == 0 and d == 0:
                        # leading zero: number not started yet
                        npprev = -1
                        nprev = -1
                        nstarted = 0
                        ladd = 0
                    else:
                        # placing an actual digit
                        nstarted = 1
                        if started == 0:
                            # first actual digit
                            npprev = -1
                            nprev = d
                            ladd = 0
                        elif pprev == -1:
                            # second actual digit
                            npprev = prev
                            nprev = d
                            ladd = 0
                        else:
                            # third or later: check if 'prev' is peak or valley
                            is_peak = prev > pprev and prev > d
                            is_valley = prev < pprev and prev < d
                            ladd = 1 if is_peak or is_valley else 0
                            npprev = prev
                            nprev = d

                    # recurse to next position
                    sc, ss = dp(pos + 1, ntight, npprev, nprev, nstarted)
                    ans_c += sc
                    # add current waviness contribution to all sub-completions
                    ans_s += ss + ladd * sc

                return ans_c, ans_s

            # start from pos 0, tight=1, no previous digits, not started
            return dp(0, 1, -1, -1, 0)[1]

        # total for range is cumulative(num2) - cumulative(num1-1)
        return sum_up_to(num2) - sum_up_to(num1 - 1)

    totalWaviness = total_waviness
