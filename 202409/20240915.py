# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/


class Solution:
    """1371. Find the Longest Substring Containing Vowels in Even Counts

    Given the string `s`, return the size of the longest substring containing each vowel
    an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even
    number of times.

    Methods:
        find_the_longest_substring(s: str) -> int:
            Finds the length of the longest substring with even counts of vowels.
    """

    def find_the_longest_substring(self, s: str) -> int:
        """
        Finds the length of the longest substring where each vowel appears an even number of times.

        Args:
            s (str): The input string to analyze.

        Returns:
            int: The length of the longest substring with even vowel counts.

        Time complexity: O(n), where n is the length of the string.
        Space complexity: O(1), as we use a fixed-size dictionary for states.
        """
        # Define vowels
        vowels = 'aeiou'

        # State mask where each bit represents the parity of a vowel
        state = 0

        # Dictionary to store the first occurrence of each state
        state_dict = {0: -1}

        max_length = 0

        for i, char in enumerate(s):
            # If char is a vowel, toggle its bit in the state
            if char in vowels:
                state ^= 1 << vowels.index(char)

            # If we've seen this state before, update max_length
            if state in state_dict:
                max_length = max(max_length, i - state_dict[state])
            else:
                # If it's a new state, record its position
                state_dict[state] = i

        return max_length

    findTheLongestSubstring = find_the_longest_substring
