# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/


class Solution:
    """3532. Path Existence Queries in a Graph I

    You are given an integer `n` representing the number of nodes in a graph, labeled
    from 0 to `n - 1`.

    You are also given an integer array `nums` of length `n` sorted in **non-
    decreasing** order, and an integer `max_diff`.

    An **undirected** edge exists between nodes `i` and `j` if the **absolute**
    difference between `nums[i]` and `nums[j]` is **at most** `max_diff` (i.e.,
    `|nums[i] - nums[j]| <= max_diff`).

    You are also given a 2D integer array `queries`. For each `queries[i] = [ui, vi]`,
    determine whether there exists a path between nodes `ui` and `vi`.

    Return a boolean array `answer`, where `answer[i]` is `true` if there exists a path
    between `ui` and `vi` in the `ith` query and `false` otherwise.

    Constraints:

    * `1 <= n == nums.length <= 105`

    * `0 <= nums[i] <= 105`

    * `nums` is sorted in **non-decreasing** order.

    * `0 <= max_diff <= 105`

    * `1 <= queries.length <= 105`

    * `queries[i] == [ui, vi]`

    * `0 <= ui, vi < n`"""

    def path_existence_queries(
        self, n: int, nums: list[int], max_diff: int, queries: list[list[int]]
    ) -> list[bool]: ...

    pathExistenceQueries = path_existence_queries
