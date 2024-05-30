# https://leetcode.com/problems/combinations/
# TODO: Submit with time travel ticket


class Solution:
    """77. Combinations

    Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers
    chosen from the range* `[1, n]`.

    You may return the answer in **any order**.

    """

    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start, path):
            # If the current combination is of size k, add it to the result
            if len(path) == k:
                # Make a copy of the current combination
                result.append(path[:])
                return

            # Generate combinations starting from 'start' to 'n'
            for i in range(start, n + 1):
                # Add the current number to the combination
                path.append(i)
                # Recursively generate combinations for the next numbers
                backtrack(i + 1, path)
                # Backtrack by removing the last number to try a different combination
                path.pop()

        result = []
        # Start the backtracking process from 1 with an empty initial combination
        backtrack(1, [])
        return result