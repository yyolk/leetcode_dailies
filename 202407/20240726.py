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
    ) -> int: ...

    findTheCity = find_the_city
