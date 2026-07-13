# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    """1331. Rank Transform of an Array
    
    Given an array of integers arr, replace each element with its rank. The rank
    represents how large the element is. The rank has the following rules:
    * Rank is an integer starting from 1.
    * The larger the element, the larger the rank. If two elements are equal,
    their rank must be the same.
    * Rank should be as small as possible.
    Constraints:
    * 0 <= arr.length <= 10^5
    * -10^9 <= arr[i] <= 10^9"""
    def array_rank_transform(self, arr: list[int]) -> list[int]:
        # Sort unique values to determine ranks efficiently
        sorted_unique = sorted(set(arr))
        # Map value to 1-based rank using dict for O(1) lookups
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}
        # Transform original array using the rank mapping
        return [rank_map[x] for x in arr]

    arrayRankTransform = array_rank_transform
