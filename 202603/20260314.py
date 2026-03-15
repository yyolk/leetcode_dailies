# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

class Solution:
    """1415. The k-th Lexicographical String of All Happy Strings of Length n

    A happy string is a string that:
    * consists only of letters of the set ['a', 'b', 'c'].
    * s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
      1-indexed).
    For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy
    strings and strings "aa", "baa" and "ababbc" are not happy strings.
    Given two integers n and k, consider a list of all happy strings of length n
    sorted in lexicographical order. Return the kth string of this list or
    return an empty string if there are less than k happy strings of length n.
    """
    def get_happy_string(self, n: int, k: int) -> str:
        # Total happy strings = 3 * 2^(n-1)
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        # Build result char by char
        result = []
        prev = None
        for i in range(n):
            # Candidates and size of strings per choice
            if i == 0:
                candidates = ["a", "b", "c"]
                subtree_size = 1 << (n - 1)
            else:
                candidates = [c for c in "abc" if c != prev]
                subtree_size = 1 << (n - i - 1)

            # Pick the candidate where k falls in its subtree
            for cand in candidates:
                if k <= subtree_size:
                    result.append(cand)
                    prev = cand
                    break
                k -= subtree_size
        return "".join(result)

    getHappyString = get_happy_string