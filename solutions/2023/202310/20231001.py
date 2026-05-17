# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    """557. Reverse Words in a String III

    Given a string `s`, reverse the order of characters in each word within a sentence while
    still preserving whitespace and initial word order.
    """

    def reverseWords(self, s: str) -> str:
        """Reverse the words while preserving whitespace and initial word order.

        Proposed solution using split and reversed.
        All joins happen at the moment of return.

        Args:
            s (str): Input string to reverse.

        Returns:
            str: The resulting special reversed string
        """
        results = []
        for word in s.split():
            # Append a reversed(...) iterator to our results list
            results.append(reversed(word))

        # Join each reversed result into a string, while joining all of them with a " "
        return " ".join("".join(result) for result in results)
