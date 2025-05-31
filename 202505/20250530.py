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

    def closest_meeting_node(self, edges: list[int], node1: int, node2: int) -> int:
        def get_distances(start: int) -> dict[int, int]:
            """Helper function to compute distances from a starting node to all reachable nodes."""
            dist = {}
            current = start
            distance = 0
            # Traverse until we hit a node with no outgoing edge or a cycle
            while current != -1 and current not in dist:
                dist[current] = distance
                next_node = edges[current]
                if next_node == -1:
                    break
                current = next_node
                distance += 1
            return dist

        # Compute distances from node1 and node2 to all reachable nodes
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        # Find nodes reachable from both node1 and node2
        common_nodes = set(dist1.keys()) & set(dist2.keys())

        # If no common nodes exist, return -1
        if not common_nodes:
            return -1

        # Find the minimum of the maximum distances from node1 and node2
        min_max_dist = min(max(dist1[node], dist2[node]) for node in common_nodes)
        # Get all nodes that achieve this minimum maximum distance
        candidates = [
            node
            for node in common_nodes
            if max(dist1[node], dist2[node]) == min_max_dist
        ]

        # Return the node with the smallest index among the candidates
        return min(candidates)

    closestMeetingNode = closest_meeting_node
