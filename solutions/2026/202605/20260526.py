# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    """3120. Count the Number of Special Characters I

    You are given a string word. A letter is called special if it appears both
    in lowercase and uppercase in word. Return the number of special letters
    in word.
    """
    def number_of_special_chars(self, word: str) -> int:
        # Collect set of lowercase letters present in word
        lowers = {c for c in word if c.islower()}
        # Collect set of uppercase letters normalized to lowercase
        uppers = {c.lower() for c in word if c.isupper()}
        # Intersection gives letters that appear in both cases
        return len(lowers & uppers)

    numberOfSpecialChars = number_of_special_chars