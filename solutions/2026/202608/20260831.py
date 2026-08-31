# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    """2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

    A critical point in a linked list is defined as either a local maxima or a
    local minima.

    A node is a local maxima if the current node has a value strictly greater
    than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller
    than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a
    previous node and a next node.

    Given a linked list head, return an array of length 2 containing
    [minDistance, maxDistance] where minDistance is the minimum distance
    between any two distinct critical points and maxDistance is the maximum
    distance between any two distinct critical points. If there are fewer than
    two critical points, return [-1, -1].

    Constraints:

    * The number of nodes in the list is in the range [2, 10^5].

    * 1 <= Node.val <= 10^5
    """

    def nodes_between_critical_points(self, head: ListNode | None) -> list[int]:
        # Collect 1-based indices of every critical point while walking the list.
        critical: list[int] = []
        prev = head
        # Start at the second node (index 2); first node cannot be critical.
        curr = head.next if head is not None else None
        index = 2

        while curr is not None and curr.next is not None:
            nxt = curr.next
            # Local max or local min.
            if (curr.val > prev.val and curr.val > nxt.val) or (
                curr.val < prev.val and curr.val < nxt.val
            ):
                critical.append(index)
            prev = curr
            curr = nxt
            index += 1

        if len(critical) < 2:
            return [-1, -1]

        # Max distance is always between the first and last critical points.
        max_distance = critical[-1] - critical[0]
        # Min distance is the smallest gap between consecutive critical points.
        min_distance = min(
            critical[i] - critical[i - 1] for i in range(1, len(critical))
        )
        return [min_distance, max_distance]

    nodesBetweenCriticalPoints = nodes_between_critical_points
