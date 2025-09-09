# https://leetcode.com/problems/number-of-people-aware-of-a-secret/


class Solution:
    """2327. Number of People Aware of a Secret

    On day `1`, one person discovers a secret.

    You are given an integer `delay`, which means that each person will **share** the
    secret with a new person **every day**, starting from `delay` days after discovering
    the secret. You are also given an integer `forget`, which means that each person
    will **forget** the secret `forget` days after discovering it. A person **cannot**
    share the secret on the same day they forgot it, or on any day afterwards.

    Given an integer `n`, return *the number of people who know the secret at the end of
    day* `n`. Since the answer may be very large, return it **modulo** `109 + 7`."""

    def people_aware_of_secret(self, n: int, delay: int, forget: int) -> int:
        # Define the modulo constant for large numbers
        MOD = 10**9 + 7
        # dp[i] represents the number of new people learning the secret on day i
        dp = [0] * (n + 1)
        # On day 1, one person learns the secret
        dp[1] = 1
        # prefix[i] will store the cumulative sum of dp[1] to dp[i]
        prefix = [0] * (n + 2)
        # Initialize prefix for day 1
        prefix[1] = 1
        # Loop through each day from 2 to n to calculate new learners
        for i in range(2, n + 1):
            # Calculate the left boundary of the window: earliest day someone could have learned to share today
            left = max(1, i - forget + 1)
            # Calculate the right boundary: latest day someone could have learned to share today
            right = i - delay
            # If valid window, compute sum using prefix; else, no new learners
            if right >= left:
                # Sum of new learners from left to right using prefix difference
                sum_val = (prefix[right] - prefix[left - 1] + MOD) % MOD
                dp[i] = sum_val
            else:
                dp[i] = 0
            # Update the prefix sum for the current day
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD
        # Calculate the left boundary for people who still know the secret on day n
        know_left = max(1, n - forget + 1)
        # Compute the number of people who know the secret: sum of new learners from know_left to n
        ans = (prefix[n] - prefix[know_left - 1] + MOD) % MOD
        return ans

    peopleAwareOfSecret = people_aware_of_secret
