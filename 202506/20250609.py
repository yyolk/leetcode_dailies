# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/


class Solution:
    """440. K-th Smallest in Lexicographical Order

    Given two integers `n` and `k`, return *the* `kth` *lexicographically smallest
    integer in the range* `[1, n]`."""

    def find_kth_number(self, n: int, k: int) -> int:
        def calc_step(cur, n):
            """Calculate the number of numbers in the subtree rooted at cur that are <= n."""
            step = 0
            a = cur
            b = cur + 1
            while a <= n:
                step += min(b, n + 1) - a
                a *= 10
                b *= 10
            return step

        cur = 1
        k -= 1  # Adjust k to be zero-based since we start at 1
        while k > 0:
            step = calc_step(cur, n)
            if step <= k:
                # If step <= k, the k-th number is not in this subtree, move to next sibling
                k -= step
                cur += 1
            else:
                # If step > k, the k-th number is in this subtree, go deeper
                cur *= 10
                k -= 1
        return cur

    findKthNumber = find_kth_number
