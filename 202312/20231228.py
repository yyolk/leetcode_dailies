# https://leetcode.com/problems/string-compression-ii/


class Solution:
    """1531. String Compression II

    [Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) is a string
    compression method that works by replacing consecutive identical characters
    (repeated 2 or more times) with the concatenation of the character and the number
    marking the count of the characters (length of the run). For example, to compress
    the string `"aabccc"` we replace `"aa"` by `"a2"` and replace `"ccc"` by `"c3"`.
    Thus the compressed string becomes `"a2bc3"`.

    Notice that in this problem, we are not adding `'1'` after single characters.

    Given a string `s` and an integer `k`. You need to delete **at most** `k` characters
    from `s` such that the run-length encoded version of `s` has minimum length.

    Find the *minimum length of the run-length encoded version of* `s` *after deleting
    at most* `k` *characters*.
    """

    def get_length_of_optimal_compression(self, s: str, k: int) -> int:
        n = len(s)

        # Initialize a 2D array to store the minimum length of encoded string for each substring
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        # Loop through the string and consider all possible deletions
        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, del_ = 0, 0

                # Iterate over previous characters to calculate counts and deletions
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_ += 1

                    # Update the minimum length using dynamic programming
                    if j - del_ >= 0:
                        dp[i][j] = min(
                            dp[i][j],
                            dp[l - 1][j - del_]
                            + 1
                            + (
                                3
                                if cnt >= 100
                                else 2
                                if cnt >= 10
                                else 1
                                if cnt >= 2
                                else 0
                            ),
                        )

                # Consider the case of not deleting the current character
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        # Return the minimum length of the run-length encoded string after considering all possible deletions
        return dp[n][k]

    getLengthOfOptimalCompression = get_length_of_optimal_compression
