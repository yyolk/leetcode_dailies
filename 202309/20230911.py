# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
from collections import defaultdict


class Solution:
    """1282. Group the People Given the Group Size They Belong To

    There are `n` people that are split into some unknown number of groups. Each person is
    labeled with a **unique ID** from `0` to `n - 1`.

    You are given an integer array `groupSizes`, where `groupSizes[i]` is the size of the
    group that person `i` is in. For example, if `groupSizes[1] = 3`, then person `1` must
    be in a group of size `3`.

    Return *a list of groups such that each person `i` is in a group of size
    `groupSizes[i]`*.

    Each person should appear in **exactly one group**, and every person must be in a group.
    If there are multiple answers, **return any of them**. It is **guaranteed** that there
    will be **at least one** valid solution for the given input.
    """

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """Responds with a mapping of groups that are valid in the input

        Proposed solution.

        Args:
            groupSizes (List of int): the input list of people implicitly id'd by their index

        Returns:
            List of List of int: the resulting valid groups that align with the constraint of the
                value at index i is the same size of group
        """
        # DefaultDict to store people grouped by their group sizes
        groups = defaultdict(list)

        # Iterate through groupSizes and append them to the appropriate size in the groups Dict
        for i, size in enumerate(groupSizes):
            groups[size].append(i)

        # Init an empty list for our result
        results = []

        # Iterate through our newly-created groups Dict
        for size, members in groups.items():
            # Ensure that each group contains exactly the required size of people
            for i in range(0, len(members), size):
                # Append subgroup to the results
                results.append(members[i : i + size])

        # Return our results
        return results
