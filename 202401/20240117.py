# https://leetcode.com/problems/unique-number-of-occurrences/
from collections import Counter


class Solution:
    """1207. Unique Number of Occurrences

    Given an array of integers `arr`, return `true` *if the number of occurrences of
    each value in the array is **unique** or* `false` *otherwise*.
    """

    def unique_occurrences(self, arr: list[int]) -> bool:
        # Create a Counter(...) from the input arr.
        counter = Counter(arr)

        # Determine if the occurences are unique.
        return len(set(counter.values())) == len(counter.values())

    uniqueOccurrences = unique_occurrences
