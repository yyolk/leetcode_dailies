# https://leetcode.com/problems/find-the-string-with-lcp

class Solution:
    """2573. Find the String with LCP

    We define the lcp matrix of any 0-indexed string word of n lowercase English
    letters as an n x n grid such that lcp[i][j] is equal to the length of the
    longest common prefix between the substrings word[i,n-1] and word[j,n-1].
    Given an n x n matrix lcp, return the alphabetically smallest string word
    that corresponds to lcp. If there is no such string, return an empty string.
    A string a is lexicographically smaller than a string b (of the same length)
    if in the first position where a and b differ, string a has a letter that
    appears earlier in the alphabet than the corresponding letter in b. For
    example, "aabd" is lexicographically smaller than "aaca" because the first
    position they differ is at the third letter, and 'b' comes before 'c'.
    """
    def find_the_string(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        # sentinel marks positions not yet assigned a letter
        sentinel = chr(ord("a") - 1)
        word = [sentinel] * n
        c = sentinel
        for i in range(n):
            if word[i] != sentinel:
                continue
            # introduce the next smallest available letter
            c = chr(ord(c) + 1)
            if c > "z":
                return ""
            # propagate this letter to all later j that must start with it
            for j in range(i, n):
                if lcp[i][j] > 0:
                    word[j] = c
        # validate that the constructed word exactly reproduces the lcp matrix
        for i in range(n):
            for j in range(n):
                # lcp of the suffixes after the first character
                next_lcp = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                # lcp must be 0 when first chars differ, else 1 + next_lcp
                curr_lcp = 1 + next_lcp if word[i] == word[j] else 0
                if lcp[i][j] != curr_lcp:
                    return ""
        return "".join(word)

    findTheString = find_the_string