# https://leetcode.com/problems/longest-balanced-substring-ii


class Solution:
    """3714. Longest Balanced Substring II
    
    You are given a string s consisting only of the characters 'a', 'b', and 'c'.
    A substring of s is called balanced if all distinct characters in the
    substring appear the same number of times.
    Return the length of the longest balanced substring of s.
    """
    def longest_balanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # Longest run of identical characters (balanced with 1 distinct char)
        streak = 0
        prev = None
        for ch in s:
            if ch == prev:
                streak += 1
            else:
                streak = 1
                prev = ch
            ans = max(ans, streak)
        
        # Balanced with 3 distinct characters (equal non-zero counts)
        seen_three = {(0, 0): -1}
        diff_ab = 0  # count_a - count_b
        diff_ac = 0  # count_a - count_c
        for i in range(n):
            if s[i] == "a":
                diff_ab += 1
                diff_ac += 1
            elif s[i] == "b":
                diff_ab -= 1
            elif s[i] == "c":
                diff_ac -= 1
            key = (diff_ab, diff_ac)
            if key in seen_three:
                ans = max(ans, i - seen_three[key])
            if key not in seen_three:
                seen_three[key] = i
        
        # Balanced with 2 distinct characters (equal non-zero counts)
        pairs = [("a", "b", "c"), ("a", "c", "b"), ("b", "c", "a")]
        for c1, c2, excl in pairs:
            i = 0
            pair_max = 0
            while i < n:
                if s[i] == excl:
                    i += 1
                    continue
                # New contiguous segment containing only c1 and c2
                seen = {0: i - 1}  # prefix 0 just before segment start
                pref = 0
                local = 0
                while i < n and s[i] != excl:
                    pref += 1 if s[i] == c1 else -1
                    if pref in seen:
                        local = max(local, i - seen[pref])
                    if pref not in seen:
                        seen[pref] = i
                    i += 1
                pair_max = max(pair_max, local)
            ans = max(ans, pair_max)
        
        return ans

    longestBalanced = longest_balanced