# https://leetcode.com/problems/kth-distinct-string-in-an-array/


class Solution:
    """2053. Kth Distinct String in an Array

    A **distinct string** is a string that is present only **once** in an array.

    Given an array of strings `arr`, and an integer `k`, return *the* `kth` ***distinct
    string** present in* `arr`. If there are **fewer** than `k` distinct strings, return
    *an **empty string*** `""`.

    Note that the strings are considered in the **order in which they appear** in the
    array.

    """

    def kth_distinct(self, arr: list[str], k: int) -> str:
        # Create a dictionary to count the occurrences of each string
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1
        
        # Iterate through the array and find the k-th distinct string
        distinct_count = 0
        for string in arr:
            if count[string] == 1:  # Check if the string is distinct
                distinct_count += 1
                if distinct_count == k:
                    return string
        
        # If there are fewer than k distinct strings, return an empty string
        return ""

    kthDistinct = kth_distinct
