# https://leetcode.com/problems/custom-sort-string/


class Solution:
    """791. Custom Sort String
    You are given two strings `order` and `s`. All the characters of `order` are **unique**
    and were sorted in some custom order previously.


    Permute the characters of `s` so that they match the order that `order` was sorted.
    More specifically, if a character `x` occurs before a character `y` in `order`, then `x`
    should occur before `y` in the permuted string.


    Return *any permutation of* `s` *that satisfies this property*.
    """

    def custom_sort_string(self, order: str, s: str) -> str:
        # Create a dictionary to store the count of each character in s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Create the custom sorted string based on the order
        custom_sorted_s = ""
        for char in order:
            if char in char_count:
                custom_sorted_s += char * char_count[char]
                del char_count[char]

        # Append the remaining characters from s (not in order) to the result
        for char, count in char_count.items():
            custom_sorted_s += char * count

        return custom_sorted_s

    customSortString = custom_sort_string
