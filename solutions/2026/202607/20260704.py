# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/


class Solution:
    """2492. Minimum Score of a Path Between Two Cities

    You are given a positive integer `n` representing `n` cities numbered from `1` to
    `n`. You are also given a **2D** array `roads` where `roads[i] = [ai, bi,
    distancei]` indicates that there is a **bidirectional** road between cities `ai` and
    `bi` with a distance equal to `distancei`. The cities graph is not necessarily
    connected.

    The **score** of a path between two cities is defined as the **minimum** distance of
    a road in this path.

    Return *the **minimum** possible score of a path between cities* `1` *and* `n`.

    **Note**:

    * A path is a sequence of roads between two cities.

    * It is allowed for a path to contain the same road **multiple** times, and you can
    visit cities `1` and `n` multiple times along the path.

    * The test cases are generated such that there is **at least** one path between `1`
    and `n`.

    Constraints:

    * `2 <= n <= 105`

    * `1 <= roads.length <= 105`

    * `roads[i].length == 3`

    * `1 <= ai, bi <= n`

    * `ai != bi`

    * `1 <= distancei <= 104`

    * There are no repeated edges.

    * There is at least one path between `1` and `n`."""

    def min_score(self, n: int, roads: list[list[int]]) -> int: ...

    minScore = min_score
