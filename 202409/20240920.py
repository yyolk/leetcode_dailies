# https://leetcode.com/problems/shortest-palindrome/


class Solution:
    """214. Shortest Palindrome

    You are given a string `s`. You can convert `s` to a palindrome by adding characters
    in front of it.

    Return *the shortest palindrome you can find by performing this transformation*.

    """

    def shortest_palindrome(self, s: str) -> str:
        if not s:  # If the string is empty, return an empty string
            return ""

        # Create a new string by concatenating s with a sentinel and its reverse
        # This helps in finding the longest palindromic prefix using string matching techniques
        rev = s[::-1]
        # '#' is used as a sentinel to avoid overlap
        temp = s + "#" + rev

        # Compute the KMP failure function or similar for our purpose
        # Here, we use a simple prefix function for clarity
        lps = [0] * len(temp)
        length = 0
        for i in range(1, len(temp)):
            while length > 0 and temp[length] != temp[i]:
                length = lps[length - 1]
            if temp[length] == temp[i]:
                length += 1
            lps[i] = length

        # The length of the longest palindromic prefix is at the end of lps array
        longest_palindrome_prefix = lps[-1]

        # If the entire string is already a palindrome, no need to add anything
        if longest_palindrome_prefix == len(s):
            return s

        # Add the reverse of the non-palindromic suffix to the front
        add = rev[:len(s) - longest_palindrome_prefix]

        return add + s

    shortestPalindrome = shortest_palindrome
