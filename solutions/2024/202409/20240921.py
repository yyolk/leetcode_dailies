# https://leetcode.com/problems/lexicographical-numbers/


class Solution:
    """386. Lexicographical Numbers

    Given an integer `n`, return all the numbers in the range `[1, n]` sorted in
    lexicographical order.

    You must write an algorithm that runs in `O(n)` time and uses `O(1)` extra space.

    """

    def lexical_order(self, n: int) -> list[int]:
        result = []

        # Current number we are checking
        current = 1

        # Loop until we've found all numbers
        for _ in range(n):
            result.append(current)

            # If 10*current is within bounds, we go 'down' in lexicographical order
            if current * 10 <= n:
                current *= 10
            # If current+1 is within bounds, we go 'right'
            elif current % 10 != 9 and current + 1 <= n:
                current += 1
            # If we've hit a 9 or gone out of bounds, we go 'up'
            else:
                # Keep dividing by 10 until we can move right
                while (current // 10) % 10 == 9:
                    current //= 10
                current = current // 10 + 1

        return result

    lexicalOrder = lexical_order
