# https://leetcode.com/problems/find-missing-elements/


class Solution:
    """3731. Find Missing Elements

    You are given an integer array `nums` consisting of **unique** integers.
    Originally, `nums` contained **every integer** within a certain range.
    However, some integers might have gone **missing** from the array.
    The **smallest** and **largest** integers of the original range are still
    present in `nums`.
    Return a **sorted** list of all the missing integers in this range. If no
    integers are missing, return an **empty** list.
    Constraints:
    * `2 <= nums.length <= 100`
    * `1 <= nums[i] <= 100`
    """

    def find_missing_elements(self, nums: list[int]) -> list[int]:
        # Determine the bounds of the original continuous range
        min_val, max_val = min(nums), max(nums)
        # Store present values for O(1) membership tests
        present = set(nums)
        # Collect missing values in ascending order (min/max are guaranteed present)
        return [x for x in range(min_val + 1, max_val) if x not in present]

    findMissingElements = find_missing_elements
