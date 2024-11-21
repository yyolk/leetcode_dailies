# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
from collections import Counter


class Solution:
    """2516. Take K of Each Character From Left and Right

    You are given a string `s` consisting of the characters `'a'`, `'b'`, and `'c'` and
    a non\\-negative integer `k`. Each minute, you may take either the **leftmost**
    character of `s`, or the **rightmost** character of `s`.

    Return *the **minimum** number of minutes needed for you to take **at least*** `k`
    *of each character, or return* `-1` *if it is not possible to take* `k` *of each
    character.*

    """

    def take_characters(self, s: str, k: int) -> int:
        # Handle the base case where k is 0
        if k == 0:
            return 0

        # Count the occurrences of each character in the string
        count_of_all_characters = Counter(s)

        # Check if there are all three characters and if there are enough of each
        if len(count_of_all_characters) < 3 or any(
            count < k for count in count_of_all_characters.values()
        ):
            return -1

        # Initialize a dictionary to keep track of excess characters taken
        count_of_excess_characters = defaultdict(int)

        # Initialize the answer (maximum length of valid substring) and left pointer
        minutes_needed, left_pointer = 0, 0

        # Iterate through the string with right pointer
        for right_pointer, character in enumerate(s):
            # Increase the count of the current character in excess
            count_of_excess_characters[character] += 1

            # While we have taken too few of the current character to meet k:
            while (
                count_of_all_characters[character]
                - count_of_excess_characters[character]
                < k
            ):
                # Decrease the count of the character at the left pointer
                count_of_excess_characters[s[left_pointer]] -= 1
                # Move the left pointer to the right
                left_pointer += 1

            # Update the maximum length of substring we can take without violating the condition
            minutes_needed = max(right_pointer - left_pointer + 1, minutes_needed)

        # Return the total length minus the maximum valid substring length
        return len(s) - minutes_needed

    takeCharacters = take_characters
