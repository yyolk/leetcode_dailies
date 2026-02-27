# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string


class Solution:
    """3666. Minimum Operations to Equalize Binary String
    
    You are given a binary string s, and an integer k. In one operation, you
    must choose exactly k different indices and flip each '0' to '1' and each
    '1' to '0'. Return the minimum number of operations required to make all
    characters in the string equal to '1'. If it is not possible, return -1.
    """
    def min_operations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count("0")
        if z == 0:
            return 0
        # maintain [cl, ch]: possible #zeros at current #ops, same parity
        cl = z
        ch = z
        for ops in range(1, n + 2):
            # min_new: min possible zeros next by flipping max zeros possible
            if ch <= k:
                min_new = k - ch
            elif cl >= k:
                min_new = cl - k
            else:
                min_new = 0
            min_new = max(0, min_new)
            # max_new: max possible zeros next by flipping min zeros possible
            peak = n - k
            if ch <= peak:
                max_new = ch + k
            elif cl >= peak:
                max_new = 2 * n - k - cl
            else:
                max_new = n
            max_new = min(n, max_new)
            next_parity = (cl + k) % 2
            nl = max(0, min_new)
            if nl % 2 != next_parity:
                nl += 1
            nh = min(n, max_new)
            if nh % 2 != next_parity:
                nh -= 1
            if nl > nh:
                return -1
            if nl <= 0 <= nh:
                return ops
            cl = nl
            ch = nh
        return -1

    minOperations = min_operations