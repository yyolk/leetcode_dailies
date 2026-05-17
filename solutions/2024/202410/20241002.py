# https://leetcode.com/problems/rank-transform-of-an-array/


class Solution:
    """1331. Rank Transform of an Array

    Given an array of integers `arr`, replace each element with its rank.

    The rank represents how large the element is. The rank has the following rules:

    * Rank is an integer starting from 1.

    * The larger the element, the larger the rank. If two elements are equal, their rank
    must be the same.

    * Rank should be as small as possible.

    """

    def array_rank_transform(self, arr: list[int]) -> list[int]:
        """
        Transform an array by replacing each element with its rank based on its value.

        This method uses a dictionary to cache ranks for efficiency, which is particularly
        beneficial when the array has duplicate values or when the array size is large.

        Args:
            arr (list[int]): The input array of integers to be ranked.

        Returns:
            list[int]: A new array where each element from 'arr' is replaced by its rank.

        Example:
            >>> s = Solution()
            >>> s.array_rank_transform([40,10,20,30])
            [4, 1, 2, 3]
        """
        # Create a sorted list of unique elements to establish rank
        sorted_arr = sorted(set(arr))
        # Use a dictionary for O(1) lookup time for ranks
        rank_dict = {value: rank + 1 for rank, value in enumerate(sorted_arr)}

        # Map each element to its rank directly from the dictionary
        return [rank_dict[element] for element in arr]

    arrayRankTransform = array_rank_transform
