# https://leetcode.com/problems/relative-sort-array/
from collections import Counter


class Solution:
    """1122. Relative Sort Array

    Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all
    elements in `arr2` are also in `arr1`.

    Sort the elements of `arr1` such that the relative ordering of items in `arr1` are
    the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the
    end of `arr1` in **ascending** order.

    """

    def relative_sort_array(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Count frequencies of each element in arr1
        arr1_counts = Counter(arr1)
        result = []

        # Add elements from arr2 to the result in the specified order
        for num in arr2:
            result += [num] * arr1_counts[num]
            del arr1_counts[num]

        # Add remaining elements not in arr2, sorted in ascending order
        remaining = sorted(arr1_counts.elements())
        result.extend(remaining)

        return result

    relativeSortArray = relative_sort_array
