# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

import bisect

class Solution:
    """3756. Concatenate Non-Zero Digits and Multiply by Sum II
    
    Given string s of digits length m and queries[i]=[li,ri], for each extract
    s[li..ri], form x by concat non-zero digits (x=0 if none), compute
    (x * sum_of_digits_of_x) % (10**9+7). Return list of answers."""
    def sum_and_multiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        # collect positions and non-zero digits for O(1) range mapping later
        nz_pos = []
        nz_d = []
        for i in range(len(s)):
            if s[i] != "0":
                nz_pos.append(i)
                nz_d.append(int(s[i]))
        k = len(nz_d)
        # prefix_num[i+1] holds number formed by nz_d[0..i] % MOD
        prefix_num = [0] * (k + 1)
        # prefix sum of digit values in nz sequence
        p_sum = [0] * (k + 1)
        # precompute 10**j % MOD up to max possible length
        pow10 = [1] * (k + 1)
        for i in range(k):
            # build left-to-right number mod
            prefix_num[i + 1] = (prefix_num[i] * 10 + nz_d[i]) % MOD
            p_sum[i + 1] = p_sum[i] + nz_d[i]
            pow10[i + 1] = pow10[i] * 10 % MOD
        answer = []
        for li, ri in queries:
            # find inclusive [L,R] indices in nz lists via bisect
            L = bisect.bisect_left(nz_pos, li)
            R = bisect.bisect_right(nz_pos, ri) - 1
            if L > R:
                answer.append(0)
                continue
            len_sub = R - L + 1
            # x = full prefix[R+1] minus prefix[L] shifted by 10^len_sub
            x = (prefix_num[R + 1] - prefix_num[L] * pow10[len_sub] % MOD + MOD) % MOD
            dsum = p_sum[R + 1] - p_sum[L]
            answer.append(x * (dsum % MOD) % MOD)
        return answer

    sumAndMultiply = sum_and_multiply
