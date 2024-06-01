# https://leetcode.com/problems/score-of-a-string/


class Solution:
    """3110. Score of a String

    You are given a string `s`. The **score** of a string is defined as the sum of the
    absolute difference between the **ASCII** values of adjacent characters.

    Return the **score** of`s`.

    """

    def score_of_string(self, s: str) -> int:
        # Use sum with a generator expression to calculate the total score
        return sum(
            # Calculate the absolute difference between the ASCII values of adjacent characters
            abs(ord(s[i]) - ord(s[i + 1]))
            # Iterate over the string from the first character to the second last character
            for i in range(len(s) - 1)
        )
        
    scoreOfString = score_of_string
