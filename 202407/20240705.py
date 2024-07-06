# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/


class Solution:
    """2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

    A **critical point** in a linked list is defined as **either** a **local maxima** or
    a **local minima**.

    A node is a **local maxima** if the current node has a value **strictly greater**
    than the previous node and the next node.

    A node is a **local minima** if the current node has a value **strictly smaller**
    than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists **both** a
    previous node and a next node.

    Given a linked list `head`, return *an array of length 2 containing* `[minDistance,
    maxDistance]` *where* `minDistance` *is the **minimum distance** between **any two
    distinct** critical points and* `maxDistance` *is the **maximum distance** between
    **any two distinct** critical points. If there are **fewer** than two critical
    points, return* `[-1, -1]`.

    Definition for singly-linked list.

        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

    """

    def nodes_between_critical_points(self, head: Optional[ListNode]) -> list[int]:
        if not head or not head.next or not head.next.next:
            # If the list has fewer than 3 nodes, there can't be any critical points
            return [-1, -1]

        critical_points = []
        prev, curr, next = head, head.next, head.next.next
        index = 1  # Start with the second node

        while next:
            # Check if the current node is a local minima or maxima
            if (curr.val > prev.val and curr.val > next.val) or (
                curr.val < prev.val and curr.val < next.val
            ):
                critical_points.append(index)

            # Move to the next set of nodes
            prev, curr, next = curr, next, next.next
            index += 1

        if len(critical_points) < 2:
            # If there are fewer than 2 critical points
            return [-1, -1]

        # Calculate minimum and maximum distances between critical points
        min_distance = float("inf")
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(
                min_distance, critical_points[i] - critical_points[i - 1]
            )

        return [min_distance, max_distance]

    nodesBetweenCriticalPoints = nodes_between_critical_points
