# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/


class Solution:
    """3734. Lexicographically Smallest Palindromic Permutation Greater
    Than Target

    You are given two strings `s` and `target`, each of length `n`,
    consisting of lowercase English letters.
    Return the lexicographically smallest string that is both a
    palindromic permutation of `s` and strictly greater than `target`.
    If no such permutation exists, return an empty string.
    Constraints:
    * `1 <= n == s.length == target.length <= 300`
    * `s` and `target` consist of only lowercase English letters.
    """

    def lex_palindromic_permutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        # A palindrome can have at most one odd-count letter
        odd = [i for i in range(26) if freq[i] & 1]
        if len(odd) > 1:
            return ""

        # The odd letter (if any) is fixed in the middle
        mid = odd[0] if odd else None
        # Remaining letters are used as first-half / second-half pairs
        for i in range(26):
            freq[i] //= 2

        half = n // 2
        ans = [""] * n

        def make_palindrome() -> str:
            # Mirror the first half; place the reserved middle if n is odd
            if mid is not None:
                ans[half] = chr(ord("a") + mid)
            for i in range(half):
                ans[n - 1 - i] = ans[i]
            return "".join(ans)

        # Copy target's first half while those letters are still available
        pos = 0
        while pos < half:
            ch = ord(target[pos]) - ord("a")
            if freq[ch] == 0:
                break
            ans[pos] = target[pos]
            freq[ch] -= 1
            pos += 1

        # Equal first half: the mirrored palindrome may already beat target
        if pos == half:
            result = make_palindrome()
            if result > target:
                return result

        # Raise the rightmost first-half index that can take a larger letter
        while True:
            if pos < half:
                start = ord(target[pos]) - ord("a") + 1
                for c in range(start, 26):
                    if freq[c]:
                        ans[pos] = chr(ord("a") + c)
                        freq[c] -= 1
                        # Fill the suffix of the first half greedily
                        dst = pos + 1
                        for letter in range(26):
                            for _ in range(freq[letter]):
                                ans[dst] = chr(ord("a") + letter)
                                dst += 1
                        return make_palindrome()
            if pos == 0:
                return ""
            # Backtrack: restore the letter used at the previous index
            pos -= 1
            freq[ord(target[pos]) - ord("a")] += 1

    lexPalindromicPermutation = lex_palindromic_permutation
