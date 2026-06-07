# https://leetcode.com/problems/lexicographical-numbers/


class Solution:
    """386. Lexicographical Numbers

    Given an integer `n`, return all the numbers in the range `[1, n]` sorted in
    lexicographical order.

    You must write an algorithm that runs in `O(n)` time and uses `O(1)` extra space."""

    def lexical_order(self, n: int) -> list[int]:
        result = []
        current = 1
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        return result

    lexicalOrder = lexical_order
