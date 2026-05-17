# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/


class Solution:
    """1758. Minimum Changes To Make Alternating Binary String

    You are given a string `s` consisting only of the characters `'0'` and `'1'`. In one
    operation, you can change any `'0'` to `'1'` or vice versa.

    The string is called alternating if no two adjacent characters are equal. For
    example, the string `"010"` is alternating, while the string `"0100"` is not.

    Return *the **minimum** number of operations needed to make* `s` *alternating*.

    Using `ord(...)` is faster than `int(...)`:

        import timeit

        char = '0'

        # Using ord()
        time_ord = timeit.timeit(lambda: ord(char), number=1000000)

        # Using int()
        time_int = timeit.timeit(lambda: int(char), number=1000000)

        print(f"Time for ord(): {time_ord}")
        print(f"Time for int(): {time_int}")

        # Time for ord(): 0.1895001000000036
        # Time for int(): 0.34928300499998954
    """

    def min_operations(self, s: str) -> int:
        n = len(s)
        # Initialize counts for '0' and '1' at even and odd positions.
        op = [0] * 2

        # Iterate through consecutive pairs of characters
        for i in range(0, n, 2):
            # Count occurrences of '0' and '1' at even positions
            op[ord(s[i]) & 1] += 1

            # Check if there's a next character at an odd position
            if i + 1 < n:
                # Count occurrences of the opposite bit at odd positions
                op[1 - (ord(s[i + 1]) & 1)] += 1

        # Return the minimum count of operations needed for '0' and '1'
        return min(op[0], op[1])

    minOperations = min_operations
