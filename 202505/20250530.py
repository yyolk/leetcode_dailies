# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/


class Solution:
    """2359. Find Closest Node to Given Two Nodes

    You are given a **directed** graph of `n` nodes numbered from `0` to `n - 1`, where
    each node has **at most one** outgoing edge.

    The graph is represented with a given **0-indexed** array `edges` of size `n`,
    indicating that there is a directed edge from node `i` to node `edges[i]`. If there
    is no outgoing edge from `i`, then `edges[i] == -1`.

    You are also given two integers `node1` and `node2`.

    Return *the **index** of the node that can be reached from both* `node1` *and*
    `node2`*, such that the **maximum** between the distance from* `node1` *to that
    node, and from* `node2` *to that node is **minimized***. If there are multiple
    answers, return the node with the **smallest** index, and if no possible answer
    exists, return `-1`.

    Note that `edges` may contain cycles."""

    def closest_meeting_node(self, edges: list[int], node1: int, node2: int) -> int: ...

    closestMeetingNode = closest_meeting_node
