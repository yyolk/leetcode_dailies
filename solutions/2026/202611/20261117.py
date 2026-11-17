# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/


class Solution:
    """2911. Minimum Changes to Make K Semi-palindromes

    Given a string s and an integer k, partition s into k substrings such
    that the letter changes needed to make each substring a semi-palindrome
    are minimized.

    Return the minimum number of letter changes required.

    A semi-palindrome is a special type of string that can be divided into
    palindromes based on a repeating pattern. To check if a string is a
    semi-palindrome:

    1. Choose a positive divisor d of the string's length. d can range from
    1 up to, but not including, the string's length. For a string of length
    1, it does not have a valid divisor as per this definition, since the
    only divisor is its length, which is not allowed.

    2. For a given divisor d, divide the string into groups where each group
    contains characters from the string that follow a repeating pattern of
    length d. Specifically, the first group consists of characters at
    positions 1, 1 + d, 1 + 2d, and so on; the second group includes
    characters at positions 2, 2 + d, 2 + 2d, etc.

    3. The string is considered a semi-palindrome if each of these groups
    forms a palindrome.

    Constraints:

    * 2 <= s.length <= 200
    * 1 <= k <= s.length / 2
    * s contains only lowercase English letters.
    """

    def minimum_changes(self, s: str, k: int) -> int:
        n = len(s)
        # Precompute min changes to make every substring a semi-palindrome.
        # cost[i][j] for s[i:j+1] (0-based, inclusive).
        INF = n + 1
        cost = [[INF] * n for _ in range(n)]

        def changes_for_d(left: int, right: int, d: int) -> int:
            # Count mismatches for the d residue classes to form palindromes.
            changes = 0
            for offset in range(d):
                l = left + offset
                r = right - d + 1 + offset
                while l < r:
                    if s[l] != s[r]:
                        changes += 1
                    l += d
                    r -= d
            return changes

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = INF
                # Try every valid divisor d < length.
                for d in range(1, length):
                    if length % d == 0:
                        min_changes = min(
                            min_changes, changes_for_d(i, j, d)
                        )
                cost[i][j] = min_changes

        # DP: dp[parts][end] = min changes to partition first `end` chars
        # into exactly `parts` semi-palindromes (each of length >= 2).
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    if dp[parts - 1][start] < INF:
                        dp[parts][end] = min(
                            dp[parts][end],
                            dp[parts - 1][start] + cost[start][end - 1],
                        )

        return dp[k][n]

    minimumChanges = minimum_changes
