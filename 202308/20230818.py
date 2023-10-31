# https://leetcode.com/problems/maximal-network-rank/


class Solution:
    """1738. Maximal Network Rank

    There is an infrastructure of `n` cities with some number of `roads` connecting
    these cities. Each `roads[i] = [ai, bi]` indicates that there is a bidirectional
    road between cities `ai` and `bi`.

    The **network rank**of **two different cities** is defined as the total number of
    **directly** connected roads to **either** city. If a road is directly connected to
    both cities, it is only counted **once**.

    The **maximal network rank** of the infrastructure is the **maximum network rank**
    of all pairs of different cities.

    Given the integer `n` and the array `roads`, return *the **maximal network rank** of
    the entire infrastructure*.
    """

    def maximal_network_rank(self, n: int, roads: list[list[int]]) -> int:
        """Calculate the maximal network rank of the entire infrastructure.

        Proposed solution using dyanmic programming.

        Args:
            n: The total number of cities in the infrastructure.
            roads: A list of road connections, where each road is represented
                as a pair of integers [ai, bi] indicating a bidirectional road between
                cities ai and bi.

        Returns:
            The maximal network rank of the entire infrastructure.

        Example:
            solution = Solution()
            n = 4
            roads = [[0, 1], [0, 3], [1, 2], [2, 3]]
            result = solution.maximal_network_rank(n, roads)
        """
        # Create a list to keep track of the network rank of each city, initialized
        # with zeros.
        city_rank = [[] for _ in range(n)]

        # Iterate through the list of roads and update the city_rank list for each road
        for road in roads:
            a, b = road
            # Increment the length for city 'a'.
            city_rank[a].append(b)
            # Increment the length for city 'b'.
            city_rank[b].append(a)

        # Initialize a variable to keep track of the maximum network rank.
        max_rank = 0
        # Iterate through pairs of different cities to calculate their network ranks.
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the network rank for pairs of different cities
                rank = len(city_rank[i]) + len(city_rank[j])
                if j in city_rank[i] or i in city_rank[j]:
                    # Remove the double-counted road
                    rank -= 1

                # Update the maximum network rank if necessary.
                max_rank = max(max_rank, rank)

        # Return the maximum network rank of the entire infrastructure.
        return max_rank

    maximalNetworkRank = maximal_network_rank
