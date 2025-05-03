# https://leetcode.com/problems/push-dominoes/


class Solution:
    """838. Push Dominoes

    There are `n` dominoes in a line, and we place each domino vertically upright. In
    the beginning, we simultaneously push some of the dominoes either to the left or to
    the right.

    After each second, each domino that is falling to the left pushes the adjacent
    domino on the left. Similarly, the dominoes falling to the right push their adjacent
    dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays still
    due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino expends no
    additional force to a falling or already fallen domino.

    You are given a string `dominoes` representing the initial state where:

    * `dominoes[i] = "L"`, if the `ith` domino has been pushed to the left,

    * `dominoes[i] = "R"`, if the `ith` domino has been pushed to the right, and

    * `dominoes[i] = "."`, if the `ith` domino has not been pushed.

    Return *a string representing the final state*."""

    def push_dominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = list(dominoes)  # Convert to list for mutability
        # Find indices of all pushed dominoes ("L" or "R")
        indices = [i for i in range(n) if dominoes[i] in "LR"]

        # If no "L" or "R", the string remains unchanged
        if not indices:
            return dominoes

        # Handle leading "."s
        if indices[0] > 0 and dominoes[indices[0]] == "L":
            for i in range(indices[0]):
                result[i] = "L"

        # Handle trailing "."s
        if indices[-1] < n - 1 and dominoes[indices[-1]] == "R":
            for i in range(indices[-1] + 1, n):
                result[i] = "R"

        # Process each segment between consecutive pushed dominoes
        for j in range(len(indices) - 1):
            left = indices[j]
            right = indices[j + 1]
            left_char = dominoes[left]
            right_char = dominoes[right]

            if left_char == "R" and right_char == "L":
                # Forces meet; split the segment
                m = right - left - 1  # Number of "."s between
                half = m // 2
                # Left half becomes "R"
                for k in range(left + 1, left + 1 + half):
                    result[k] = "R"
                # Right half becomes "L"
                for k in range(right - half, right):
                    result[k] = "L"
                # Middle stays "." if m is odd (handled implicitly)
            elif left_char == "R" and right_char == "R":
                # All become "R"
                for k in range(left + 1, right):
                    result[k] = "R"
            elif left_char == "L" and right_char == "L":
                # All become "L"
                for k in range(left + 1, right):
                    result[k] = "L"
            elif left_char == "L" and right_char == "R":
                # All remain "." (no change needed)
                pass

        return "".join(result)  # Convert back to string

    pushDominoes = push_dominoes
