# https://leetcode.com/problems/maximum-total-importance-of-roads/


class Solution:
    """2285. Maximum Total Importance of Roads

    You are given an integer `n` denoting the number of cities in a country. The cities
    are numbered from `0` to `n - 1`.

    You are also given a 2D integer array `roads` where `roads[i] = [ai, bi]` denotes
    that there exists a **bidirectional** road connecting cities `ai` and `bi`.

    You need to assign each city with an integer value from `1` to `n`, where each value
    can only be used **once**. The **importance** of a road is then defined as the
    **sum** of the values of the two cities it connects.

    Return *the **maximum total importance** of all roads possible after assigning the
    values optimally.*

    """

    def maximum_importance(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Count the degree of each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        # Step 2: Sort cities by degree in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)

        # Step 3: Assign values to cities
        values = [0] * n
        for i in range(n):
            values[sorted_cities[i]] = n - i

        # Step 4: Calculate the total importance
        total_importance = 0
        for a, b in roads:
            total_importance += values[a] + values[b]

        return total_importance

    maximumImportance = maximum_importance
