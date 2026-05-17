# https://leetcode.com/problems/count-the-number-of-powerful-integers/


class Solution:
    """2999. Count the Number of Powerful Integers

    You are given three integers `start`, `finish`, and `limit`. You are also given a
    **0-indexed** string `s` representing a **positive** integer.

    A **positive** integer `x` is called **powerful** if it ends with `s` (in other
    words, `s` is a **suffix** of `x`) and each digit in `x` is at most `limit`.

    Return *the **total** number of powerful integers in the range* `[start..finish]`.

    A string `x` is a suffix of a string `y` if and only if `x` is a substring of `y`
    that starts from some index (**including** `0`) in `y` and extends to the index
    `y.length - 1`. For example, `25` is a suffix of `5125` whereas `512` is not."""

    def number_of_powerful_int(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        def count(N: int) -> int:
            """Helper function to count powerful integers <= N."""
            if N < 0:
                return 0  # No powerful integers less than 0
            str_N = str(N)
            len_N = len(str_N)
            k = len(s)
            if k > len_N:
                return 0  # If s is longer than N, no number <= N can end with s

            total = 0
            # Part 1: Count powerful integers with d digits where k <= d < len_N
            if k < len_N:
                total += 1  # For d = k, the number is s itself
                for d in range(k + 1, len_N):
                    # For d > k: prefix of length (d - k), first digit 1 to limit, rest 0 to limit
                    total += limit * (limit + 1) ** (d - k - 1)

            # Part 2: Count powerful integers with exactly len_N digits <= N using DP
            digits_N = [int(c) for c in str_N]
            digits_s = [int(c) for c in s]
            dp = [[0] * 2 for _ in range(len_N + 1)]
            dp[len_N][0] = 1  # Base case: empty suffix, less than N
            dp[len_N][1] = 1  # Base case: equal to N so far

            for pos in range(len_N - 1, -1, -1):
                for is_tight in [0, 1]:
                    if pos >= len_N - k:
                        # Suffix positions: must match s
                        digit = digits_s[pos - (len_N - k)]
                        if is_tight and digit > digits_N[pos]:
                            dp[pos][is_tight] = 0  # Digit exceeds N's digit, invalid
                        else:
                            new_tight = is_tight and (digit == digits_N[pos])
                            dp[pos][is_tight] = dp[pos + 1][new_tight]
                    else:
                        # Prefix positions: choose digits freely
                        ans = 0
                        low = 1 if pos == 0 else 0  # First digit can't be 0
                        for d in range(low, limit + 1):
                            if is_tight and d > digits_N[pos]:
                                break  # Exceeds N, stop
                            new_tight = is_tight and (d == digits_N[pos])
                            ans += dp[pos + 1][new_tight]
                        dp[pos][is_tight] = ans
            return total + dp[0][1]

        return count(finish) - count(start - 1)

    numberOfPowerfulInt = number_of_powerful_int
