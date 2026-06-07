# https://leetcode.com/problems/reorganize-string/
import heapq
from collections import Counter


class Solution:
    """767. Reorganize String

    Given a string s, rearrange the characters of s so that any two
    adjacent characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.
    """

    def reorganizeString(self, s: str) -> str:
        """Implemented solution to reorganize string

        Args:
            s (str): the string to rearrange

        Returns:
            str: any possible rearrangement of `s` or `""` if not possible
        """
        # Count the frequency of each character in the input string
        char_count = Counter(s)

        # Create a max heap (priority queue) with negative counts and characters
        # This will help us pop the characters with the highest frequency first
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        # Empty string to hold the reararrangement
        result = ""

        # Remember the previous count and character
        prev_count = 0
        prev_char = ""

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result += char

            # Push the previous character back into the heap if its count is negative
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            count += 1
            prev_count = count
            prev_char = char

        # If the length of the result is not the same as the input string, rearrangement is not possible
        if len(result) != len(s):
            return ""

        # Convert the resulting list back into a string
        return result
