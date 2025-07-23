# https://leetcode.com/problems/maximum-score-from-removing-substrings/


class Solution:
    """1717. Maximum Score From Removing Substrings

    You are given a string `s` and two integers `x` and `y`. You can perform two types
    of operations any number of times.

    * Remove substring `"ab"` and gain `x` points.

      + For example, when removing `"ab"` from `"cabxbae"` it becomes `"cxbae"`.

    * Remove substring `"ba"` and gain `y` points.

      + For example, when removing `"ba"` from `"cabxbae"` it becomes `"cabxe"`.

    Return *the maximum points you can gain after applying the above operations on* `s`.
    """

    def maximum_gain(self, s: str, x: int, y: int) -> int:
        # Define helper function to remove pairs and calculate score
        def remove_pairs(input_str: str, first_char: str, second_char: str, points: int):
            # Initialize stack to track characters
            stack = []
            # Initialize score for removed pairs
            score = 0
            # Iterate through each character in the input string
            for c in input_str:
                # Check if current character forms a pair with the last character in stack
                if stack and stack[-1] == first_char and c == second_char:
                    # Remove the last character from stack
                    stack.pop()
                    # Add points for the removed pair
                    score += points
                else:
                    # Add current character to stack if no pair is formed
                    stack.append(c)
            # Return total score and remaining string
            return score, ''.join(stack)

        # Determine which pair to remove first based on points
        if x >= y:
            # Remove "ab" pairs first if x points are higher or equal
            pri_score, remaining = remove_pairs(s, 'a', 'b', x)
            # Remove "ba" pairs from remaining string
            sec_score, _ = remove_pairs(remaining, 'b', 'a', y)
        else:
            # Remove "ba" pairs first if y points are higher
            pri_score, remaining = remove_pairs(s, 'b', 'a', y)
            # Remove "ab" pairs from remaining string
            sec_score, _ = remove_pairs(remaining, 'a', 'b', x)
        # Return total score from both removals
        return pri_score + sec_score

    maximumGain = maximum_gain
