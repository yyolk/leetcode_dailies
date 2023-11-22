# https://leetcode.com/problems/majority-element-ii/
from collections import Counter


class Solution:
    """229. Majority Element II

    Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋`
    times.
    """

    def majorityElement(self, nums: list[int]) -> list[int]:
        """Finds the elements that appear more than 1/3 of the times

        Proposed solution, using a collections.Counter and a filter(...) to create the
        results from a generator expression.

        Args:
            nums (list of int): The input numbers list of elements to find majority.

        Returns:
            list of int: All elements that appear more than 1/3 of the time.
        """
        n = len(nums)
        counter = Counter(nums)
        # Generate our results list(...) a generator expression from the filtered
        # Counter.items() where {key: value} is {num: occurences}
        return list(num for num, _ in filter(lambda x: x[1] > n / 3, counter.items()))
