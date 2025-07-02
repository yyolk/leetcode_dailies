# https://leetcode.com/problems/find-the-original-typed-string-ii/


class Solution:
    """3333. Find the Original Typed String II

    Alice is attempting to type a specific string on her computer. However, she tends to
    be clumsy and **may** press a key for too long, resulting in a character being typed
    **multiple** times.

    You are given a string `word`, which represents the **final** output displayed on
    Alice's screen. You are also given a **positive** integer `k`.

    Return the total number of *possible* original strings that Alice *might* have
    intended to type, if she was trying to type a string of size **at least** `k`.

    Since the answer may be very large, return it **modulo** `109 + 7`."""

    def possible_string_count(self, word: str, k: int) -> int:
        MOD = 1_000_000_007
        
        # Step 1: Parse the runs
        runs = []
        if word:
            current_char = word[0]
            count = 1
            for char in word[1:]:
                if char == current_char:
                    count += 1
                else:
                    runs.append(count)
                    current_char = char
                    count = 1
            runs.append(count)  # Append the last run
        
        m = len(runs)
        
        # Step 2: Compute total number of ways
        prod = 1
        for ri in runs:
            prod = (prod * ri) % MOD
        
        # Step 3: If m >= k, all combinations are valid
        if m >= k:
            return prod
        
        # Step 4: Dynamic Programming for m < k
        S = 2000  # k <= 2000, so t = k - m - 1 <= 1999
        prev = [0] * (S + 1)
        prev[0] = 1  # Base case: empty sum is 1 way
        
        for i in range(1, m + 1):
            curr = [0] * (S + 1)
            curr[0] = prev[0]  # n_i = 0
            for s in range(1, S + 1):
                curr[s] = (curr[s - 1] + prev[s]) % MOD
                if s - runs[i - 1] >= 0:
                    curr[s] = (curr[s] - prev[s - runs[i - 1]] + MOD) % MOD
            prev = curr
        
        # Step 5: Compute number of ways where sum m_i < k
        t = k - m - 1  # sum n_i <= k - m - 1
        if t >= 0:
            sum_dp = sum(prev[:t + 1]) % MOD
        else:
            sum_dp = 0  # No ways if t < 0, since sum n_i >= 0
        
        # Step 6: Final answer
        answer = (prod - sum_dp) % MOD
        return answer

    possibleStringCount = possible_string_count
