# https://leetcode.com/problems/count-the-number-of-consistent-strings/


class Solution:
    """1684. Count the Number of Consistent Strings

    You are given a string `allowed` consisting of **distinct** characters and an array
    of strings `words`. A string is **consistent** if all characters in the string
    appear in the string `allowed`.

    Return *the number of **consistent** strings in the array* `words`.

    """

    def count_consistent_strings(self, allowed: str, words: list[str]) -> int:
        # Convert the allowed string to a set for O(1) lookup time
        allowed_set = set(allowed)

        # Count of consistent strings
        consistent_count = 0

        for word in words:
            # Check if all characters in word are in allowed_set
            if all(char in allowed_set for char in word):
                consistent_count += 1

        return consistent_count

    countConsistentStrings = count_consistent_strings
