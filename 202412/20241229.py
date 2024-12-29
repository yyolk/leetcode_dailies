# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
MOD = 10**9 + 7


class Solution:
    """1639. Number of Ways to Form a Target String Given a Dictionary

    You are given a list of strings of the **same length** `words` and a string
    `target`.

    Your task is to form `target` using the given `words` under the following rules:

    * `target` should be formed from left to right.

    * To form the `ith` character (**0-indexed**) of `target`, you can choose the `kth`
    character of the `jth` string in `words` if `target[i] = words[j][k]`.

    * Once you use the `kth` character of the `jth` string of `words`, you **can no
    longer** use the `xth` character of any string in `words` where `x <= k`. In other
    words, all characters to the left of or at index `k` become unusuable for every
    string.

    * Repeat the process until you form the string `target`.

    **Notice** that you can use **multiple characters** from the **same string** in
    `words` provided the conditions above are met.

    Return *the number of ways to form `target` from `words`*. Since the answer may be
    too large, return it **modulo** `109 + 7`."""

    def num_ways(self, words: list[str], target: str) -> int:
        m, n = len(target), len(words[0])
        
        # Count occurrences of each character at each position
        counts = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, c in enumerate(word):
                counts[i][ord(c) - ord("a")] += 1
        
        # dp[i][j] represents the number of ways to form the first j characters of target using the first i characters of any word
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base case: there's one way to form an empty target string
        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If we don't use the current character from words
                dp[i][j] = dp[i - 1][j]
                # If we can use the current character from words
                if counts[i - 1][ord(target[j - 1]) - ord("a")] > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * counts[i - 1][ord(target[j - 1]) - ord("a")]) % MOD
        
        return dp[n][m]

    numWays = num_ways
