# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/


class Solution:
    """3534. Path Existence Queries in a Graph II

    You are given an integer `n` representing the number of nodes in a graph, labeled
    from 0 to `n - 1`.

    You are also given an integer array `nums` of length `n` and an integer `max_diff`.

    An **undirected** edge exists between nodes `i` and `j` if the **absolute**
    difference between `nums[i]` and `nums[j]` is **at most** `max_diff` (i.e.,
    `|nums[i] - nums[j]| <= max_diff`).

    You are also given a 2D integer array `queries`. For each `queries[i] = [ui, vi]`,
    find the **minimum** distance between nodes `ui` and `vi`. If no path exists between
    the two nodes, return -1 for that query.

    Return an array `answer`, where `answer[i]` is the result of the `ith` query.

    **Note:** The edges between the nodes are unweighted.

    Constraints:

    * `1 <= n == nums.length <= 105`

    * `0 <= nums[i] <= 105`

    * `0 <= max_diff <= 105`

    * `1 <= queries.length <= 105`

    * `queries[i] == [ui, vi]`

    * `0 <= ui, vi < n`"""

    def path_existence_queries(
        self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]
    ) -> list[int]: ...

    pathExistenceQueries = path_existence_queries
