# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/


class Solution:
    """2472. Maximum Number of Non-overlapping Palindrome Substrings

    You are given a string `s` and a **positive** integer `k`.

    Select a set of **non-overlapping** substrings from the string `s` that satisfy the
    following conditions:

    * The **length** of each substring is **at least** `k`.

    * Each substring is a **palindrome**.

    Return *the **maximum** number of substrings in an optimal selection*.

    A **substring** is a contiguous sequence of characters within a string.

    Constraints:

    * `1 <= k <= s.length <= 2000`

    * `s` consists of lowercase English letters.
    """

    def max_palindromes(self, s: str, k: int) -> int:
        # Any palindrome of length >= k contains a palindrome of length k or k+1.
        n = len(s)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        count = 0
        i = 0
        while i + k <= n:
            # Prefer the shortest valid palindrome starting at i (length k, else k+1).
            if is_palindrome(i, i + k - 1):
                count += 1
                i += k
            elif i + k < n and is_palindrome(i, i + k):
                count += 1
                i += k + 1
            else:
                i += 1
        return count

    maxPalindromes = max_palindromes
