# https://leetcode.com/problems/binary-prefix-divisible-by-5/


class Solution:
    """1018. Binary Prefix Divisible By 5

    Given a binary array nums, for each prefix nums[0..i], interpret it as a
    binary number xi and return a boolean list where answer[i] is true if xi
    is divisible by 5.

    Example: nums = [1,0,1] → x0 = 1, x1 = 2 (10₂), x2 = 5 (101₂)
    """
    def prefixes_div_by_5(self, nums: list[int]) -> list[bool]:
        ans = []           # result list
        cur = 0            # running value of the prefix interpreted as decimal
        
        for bit in nums:
            # Update current number: cur = (cur * 2 + bit)
            cur = (cur << 1) | bit
            # We only care about cur % 5; keep it small to avoid overflow
            cur %= 5
            # xi is divisible by 5 iff cur % 5 == 0
            ans.append(cur == 0)
        
        return ans

    prefixesDivBy5 = prefixes_div_by_5