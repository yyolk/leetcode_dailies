# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/


class Solution:
    """440. K-th Smallest in Lexicographical Order

    Given two integers `n` and `k`, return *the* `kth` *lexicographically smallest
    integer in the range* `[1, n]`.

    """

    def find_kth_number(self, n: int, k: int) -> int:
        def count_numbers(prefix, n):
            """Count numbers from prefix*10 to (prefix+1)*10 - 1 or n if smaller."""
            first_number = prefix
            next_number = prefix + 1
            total_count = 0

            while first_number <= n:
                total_count += min(n + 1, next_number) - first_number
                first_number *= 10
                next_number *= 10

            return total_count

        current = 1
        k -= 1  # Since we start at 1, we adjust k to find the (k-1)-th successor
        while k > 0:
            count = count_numbers(current, n)
            if count <= k:
                k -= count
                current += 1
            else:
                # Move down to the next level in the trie
                current *= 10
                k -= 1  # Moving down one level in our virtual trie

        return current

    findKthNumber = find_kth_number
