# https://leetcode.com/problems/maximize-active-section-with-trade-i/
class Solution:
    """3499. Maximize Active Section with Trade I
    
    You are given a binary string `s` of length `n`, where:
    * `'1'` represents an **active** section.
    * `'0'` represents an **inactive** section.
    You can perform **at most one trade** to maximize the number of
    active sections in `s`. In a trade, you:
    * Convert a contiguous block of `'1'`s that is surrounded by
    `'0'`s to all `'0'`s.
    * Afterward, convert a contiguous block of `'0'`s that is
    surrounded by `'1'`s to all `'1'`s.
    Return the **maximum** number of active sections in `s` after
    making the optimal trade.
    **Note:** Treat `s` as if it is **augmented** with a `'1'` at both
    ends, forming `t = '1' + s + '1'`. The augmented `'1'`s **do not**
    contribute to the final count.
    Constraints:
    * `1 <= n == s.length <= 105`
    * `s[i]` is either `'0'` or `'1'`
    """
    def max_active_sections_after_trade(self, s: str) -> int:
        # original count of active sections + max zeros gained by trade
        n = len(s)
        ans = 0
        # previous zero-group length; -inf so first zero never contributes alone
        pre = float("-inf")
        # max sum of lengths of any two consecutive zero-groups
        mx = 0
        i = 0
        while i < n:
            # find end of current run of identical characters
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            # length of the current group
            cur = j - i
            if s[i] == "1":
                # accumulate all original ones
                ans += cur
            else:
                # candidate gain is previous zeros + current zeros
                mx = max(mx, pre + cur)
                pre = cur
            i = j
        # trade nets the zeros of the chosen pair (intervening ones restored)
        return ans + mx

    maxActiveSectionsAfterTrade = max_active_sections_after_trade
