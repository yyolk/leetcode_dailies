# https://leetcode.com/problems/24-game/


class Solution:
    """679. 24 Game

    You are given an integer array `cards` of length `4`. You have four cards, each
    containing a number in the range `[1, 9]`. You should arrange the numbers on these
    cards in a mathematical expression using the operators `['+', '-', '*', '/']` and
    the parentheses `'('` and `')'` to get the value 24.

    You are restricted with the following rules:

    * The division operator `'/'` represents real division, not integer division.

      + For example, `4 / (1 - 2 / 3) = 4 / (1 / 3) = 12`.

    * Every operation done is between two numbers. In particular, we cannot use `'-'` as
    a unary operator.

      + For example, if `cards = [1, 1, 1, 1]`, the expression `"-1 - 1 - 1 - 1"` is
    **not allowed**.

    * You cannot concatenate numbers together

      + For example, if `cards = [1, 2, 1, 2]`, the expression `"12 + 12"` is not valid.

    Return `true` if you can get such expression that evaluates to `24`, and `false`
    otherwise."""

    def judge_point24(self, cards: list[int]) -> bool:
        # Convert integers to floats to handle divisions accurately
        nums = [float(card) for card in cards]
        # Define a small epsilon for floating-point comparisons
        EPS = 1e-6
        # Define a recursive helper function that takes the current list of numbers
        def helper(current: list[float]) -> bool:
            # If only one number left, check if it's approximately 24
            if len(current) == 1:
                return abs(current[0] - 24) < EPS
            # Iterate over all unique pairs of indices (i < j)
            for i in range(len(current)):
                for j in range(i + 1, len(current)):
                    # Extract the two numbers
                    a, b = current[i], current[j]
                    # Create a new list excluding the two selected numbers
                    new_current = [current[k] for k in range(len(current)) if k != i and k != j]
                    # List all possible operation results: a+b, a-b, b-a, a*b
                    ops = [a + b, a - b, b - a, a * b]
                    # Add a/b if b != 0
                    if abs(b) > EPS:
                        ops.append(a / b)
                    # Add b/a if a != 0
                    if abs(a) > EPS:
                        ops.append(b / a)
                    # For each possible result from the operations
                    for val in ops:
                        # Add the result to the new list
                        new_current.append(val)
                        # Recurse to see if this leads to 24
                        if helper(new_current):
                            return True
                        # Backtrack: remove the added value
                        new_current.pop()
            # If no combination works, return False
            return False
        # Start the recursion with the initial list
        return helper(nums)

    judgePoint24 = judge_point24
