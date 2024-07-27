# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/


class Solution:
    """1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

    There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where
    `edges[i] = [fromi, toi, weighti]` represents a bidirectional and weighted edge
    between cities `fromi` and `toi`, and given the integer `distance_threshold`.

    Return the city with the smallest number of cities that are reachable through some
    path and whose distance is **at most** `distance_threshold`, If there are multiple
    such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities ***i*** and ***j*** is equal to
    the sum of the edges' weights along that path.

    """

    def find_the_city(
        self, n: int, edges: list[list[int]], distance_threshold: int
    ) -> int:
        # Initialize the distance matrix
        dist = [[float("inf")] * n for _ in range(n)]

        # Set the distance from each city to itself to 0
        for i in range(n):
            dist[i][i] = 0

        # Fill the distance matrix with the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Apply the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Initialize variables to track the result
        min_neighbors = float("inf")
        result_city = -1

        # Count the number of reachable cities within the distance threshold for each city
        for i in range(n):
            count = sum(
                1 for j in range(n) if i != j and dist[i][j] <= distance_threshold
            )
            if count < min_neighbors or (count == min_neighbors and i > result_city):
                min_neighbors = count
                result_city = i

        return result_city

    findTheCity = find_the_city
