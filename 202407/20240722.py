# https://leetcode.com/problems/sort-the-people/


class Solution:
    """2418. Sort the People

    You are given an array of strings `names`, and an array `heights` that consists of
    **distinct** positive integers. Both arrays are of length `n`.

    For each index `i`, `names[i]` and `heights[i]` denote the name and height of the
    `ith` person.

    Return `names` *sorted in **descending** order by the people's heights*.

    """

    def sort_people(self, names: list[str], heights: list[int]) -> list[str]:
        # Combine names and heights into a list of tuples
        combined = list(zip(heights, names))
        
        # Sort the combined list by height in descending order
        combined.sort(reverse=True, key=lambda x: x[0])
        
        # Extract the names from the sorted combined list
        sorted_names = [name for _, name in combined]
        
        return sorted_names

    sortPeople = sort_people
