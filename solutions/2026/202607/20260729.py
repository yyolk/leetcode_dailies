# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution:
    """3518. Smallest Palindromic Rearrangement II

    You are given a palindromic string s and an integer k.
    Return the k-th lexicographically smallest palindromic permutation of s.
    If there are fewer than k distinct palindromic permutations, return an empty
    string.

    Note: Different rearrangements that yield the same palindromic string are
    considered identical and are counted once.

    Constraints:
    * 1 <= s.length <= 10^4
    * s consists of lowercase English letters.
    * s is guaranteed to be a palindrome.
    * 1 <= k <= 10^6
    """
    def smallest_palindrome(self, s: str, k: int) -> str:
        # Count character frequencies
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        # Determine middle character (at most one odd count) and half frequencies
        mid = ""
        half = [0] * 26
        for i in range(26):
            if freq[i] % 2 == 1:
                mid = chr(i + ord("a"))
            half[i] = freq[i] // 2

        n = sum(half)  # length of first half

        def count_perms(counts: list[int], length: int, limit: int) -> int:
            # Number of distinct permutations of multiset, capped at limit+1
            if length == 0:
                return 1
            res = 1
            rem = length
            for cnt in counts:
                if cnt <= 0:
                    continue
                # C(rem, cnt) via smaller side to keep intermediates <= final
                c = min(cnt, rem - cnt)
                for i in range(c):
                    res *= (rem - i)
                    res //= (i + 1)
                    if res > limit:
                        return limit + 1
                rem -= cnt
            return res

        # Check if enough distinct half-permutations
        if count_perms(half, n, k) < k:
            return ""

        # Build the k-th lex smallest first half
        first = []
        counts = half[:]
        for pos in range(n):
            for i in range(26):
                if counts[i] == 0:
                    continue
                counts[i] -= 1
                ways = count_perms(counts, n - pos - 1, k)
                if ways >= k:
                    first.append(chr(i + ord("a")))
                    break
                k -= ways
                counts[i] += 1

        left = "".join(first)
        return left + mid + left[::-1]

    smallestPalindrome = smallest_palindrome
