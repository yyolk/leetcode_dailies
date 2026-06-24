# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

class Solution:
    """3700. Number of ZigZag Arrays II
    
    You are given three integers n, l, and r. A ZigZag array of length n is
    defined as follows: each element in [l, r], no two adjacent equal, no three
    consecutive elements form a strictly increasing or strictly decreasing
    sequence. Return total valid ZigZag arrays modulo 10^9+7. Strictly
    increasing: each > previous. Strictly decreasing: each < previous.
    Constraints: 3<=n<=10^9, 1<=l<r<=75"""
    def zig_zag_arrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        S = 2 * m
        # transition matrix M[to][from] = 1 if valid next state
        M = [[0] * S for _ in range(S)]
        for j in range(m):
            p_up = j * 2
            p_down = j * 2 + 1
            # from last-up: only to k < j with new-dir down
            for k in range(j):
                M[k * 2 + 1][p_up] = 1
            # from last-down: only to k > j with new-dir up
            for k in range(j + 1, m):
                M[k * 2][p_down] = 1
        # init vector for all length-2 sequences (sets initial dir)
        V = [0] * S
        for j in range(m):
            V[j * 2] = j
            V[j * 2 + 1] = m - 1 - j
        def mat_mul(a, b, mod):
            # matrix multiply with early skip for speed
            ra = len(a)
            ca = len(a[0])
            cb = len(b[0])
            res = [[0] * cb for _ in range(ra)]
            for i in range(ra):
                for k in range(ca):
                    if a[i][k] == 0:
                        continue
                    aik = a[i][k]
                    for j in range(cb):
                        res[i][j] = (res[i][j] + aik * b[k][j]) % mod
            return res
        def mat_pow(mat, exp, mod):
            # fast exponentiation for transition matrix
            sz = len(mat)
            res = [[1 if i == j else 0 for j in range(sz)] for i in range(sz)]
            while exp:
                if exp & 1:
                    res = mat_mul(res, mat, mod)
                mat = mat_mul(mat, mat, mod)
                exp >>= 1
            return res
        if n == 2:
            return sum(V) % MOD
        # M^(n-2) advances from length 2 to length n
        powered = mat_pow(M, n - 2, MOD)
        # final = powered @ V
        new_v = [0] * S
        for i in range(S):
            for k in range(S):
                new_v[i] = (new_v[i] + powered[i][k] * V[k]) % MOD
        return sum(new_v) % MOD

    zigZagArrays = zig_zag_arrays