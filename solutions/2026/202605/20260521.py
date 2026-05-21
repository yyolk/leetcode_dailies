# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

class Solution:
    """3043. Find the Length of the Longest Common Prefix

    You are given two arrays with positive integers arr1 and arr2.
    A prefix of a positive integer is an integer formed by one or more of its
    digits, starting from its leftmost digit. For example, 123 is a prefix of
    the integer 12345, while 234 is not.
    A common prefix of two integers a and b is an integer c, such that c is a
    prefix of both a and b. For example, 5655359 and 56554 have common prefixes
    565 and 5655 while 1223 and 43456 do not have a common prefix.
    You need to find the length of the longest common prefix between all pairs
    of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
    Return the length of the longest common prefix among all pairs. If no
    common prefix exists among them, return 0.
    """
    def longest_common_prefix(self, arr1: list[int], arr2: list[int]) -> int:
        # Insert shorter list into trie to optimize memory usage
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        # Build trie with strings of numbers from arr1
        root = {}
        for num in arr1:
            node = root
            for char in str(num):
                if char not in node:
                    node[char] = {}
                node = node[char]

        # Query each number in arr2 for longest matching prefix
        max_len = 0
        for num in arr2:
            node = root
            length = 0
            for char in str(num):
                if char in node:
                    node = node[char]
                    length += 1
                    max_len = max(max_len, length)
                else:
                    break

        return max_len

    longestCommonPrefix = longest_common_prefix