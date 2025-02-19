# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/


class Solution:
    """1415. The k-th Lexicographical String of All Happy Strings of Length n

    A **happy string** is a string that:

    * consists only of letters of the set `["a", "b", "c"]`.

    * `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is
    1-indexed).

    For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings
    and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

    Given two integers `n` and `k`, consider a list of all happy strings of length `n`
    sorted in lexicographical order.

    Return *the kth string* of this list or return an **empty string** if there are less
    than `k` happy strings of length `n`."""

    def get_happy_string(self, n: int, k: int) -> str:
        # Available characters
        chars = ["a", "b", "c"]
        
        # DP table: dp[i][j] = number of happy strings of length i starting with chars[j]
        dp = [[0] * 3 for _ in range(n + 1)]
        
        # Base case: length 1
        for j in range(3):
            dp[1][j] = 1
        
        # Fill DP table for lengths 2 to n
        for i in range(2, n + 1):
            for j in range(3):
                for prev_j in range(3):
                    if j != prev_j:
                        dp[i][j] += dp[i - 1][prev_j]
        
        # Total number of happy strings of length n
        total = sum(dp[n][j] for j in range(3))
        if k > total:
            return ""
        
        # Construct the k-th happy string
        result = []
        # Index of the current character
        current_char_index = -1
        for length in range(n, 0, -1):
            for j in range(3):
                # First character
                if length == n:
                    if k <= dp[n][j]:
                        current_char_index = j
                        break
                    k -= dp[n][j]
                # Subsequent characters
                else:
                    if current_char_index != j and k <= dp[length][j]:
                        current_char_index = j
                        break
                    elif current_char_index != j:
                        k -= dp[length][j]
            result.append(chars[current_char_index])
        
        return "".join(result)

    getHappyString = get_happy_string
