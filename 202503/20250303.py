# https://leetcode.com/problems/partition-array-according-to-given-pivot/


class Solution:
    """2161. Partition Array According to Given Pivot

    You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange
    `nums` such that the following conditions are satisfied:

    * Every element less than `pivot` appears **before** every element greater than
    `pivot`.

    * Every element equal to `pivot` appears **in between** the elements less than and
    greater than `pivot`.

    * The **relative order** of the elements less than `pivot` and the elements greater
    than `pivot` is maintained.

      + More formally, consider every `pi`, `pj` where `pi` is the new position of the
    `ith` element and `pj` is the new position of the `jth` element. If `i < j` and
    **both** elements are smaller (*or larger*) than `pivot`, then `pi < pj`.

    Return `nums` *after the rearrangement.*"""

    def pivot_array(self, nums: list[int], pivot: int) -> list[int]:
        # Initialize three lists to hold elements less than, equal to, and greater than the pivot
        less = []
        equal = []
        greater = []

        # Iterate through each element in the input array
        for x in nums:
            # If the element is less than the pivot, append it to the 'less' list
            if x < pivot:
                less.append(x)
            # If the element is equal to the pivot, append it to the 'equal' list
            elif x == pivot:
                equal.append(x)
            # If the element is greater than the pivot, append it to the 'greater' list
            else:
                greater.append(x)

        # Concatenate the three lists: less + equal + greater to form the final array
        return less + equal + greater

    pivotArray = pivot_array
