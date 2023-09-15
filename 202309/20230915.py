# https://leetcode.com/problems/min-cost-to-connect-all-points/


class Solution:
    """1584. Min Cost to Connect All Points

    You are given an array `points` representing integer coordinates of some points on a
    2D-plane, where `points[i] = [xi, yi]`.

    The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan
    distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute
    value of `val`.

    Return *the minimum cost to make all points connected.* All points are connected if
    there is **exactly one** simple path between any two points.
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Minimum cost to connect all points

        Proposed solution using spanning trees, edges, and disjoint-set data structure.

        Args:
            points (List of List of int): the input points to connect, in x,y pairs

        Returns:
            int: the minimum cost to connect all points utilizing manhattan distance
        """

        def manhattan_distance(point1, point2):
            """Calculates the Manhattan distance between two points"""
            x1, y1 = point1
            x2, y2 = point2
            return abs(x1 - x2) + abs(y1 - y2)

        def find(parent, i):
            """Find the root parent of a set containing point i"""
            if parent[i] == i:
                return i
            parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, i, j):
            """Merge two sets by updating their parent pointers"""
            root_i = find(parent, i)
            root_j = find(parent, j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Initialize an empty edges list
        edges = []
        # n is the length of our input
        n = len(points)

        # Form the edges list, representing distances between all pairs of points
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((i, j, distance))

        # Sort edges by distance
        edges.sort(key=lambda x: x[2])

        # Initialize a list for the disjoint-set data structure
        parent = list(range(n))
        # Initialize vars for tracking the cost and connected_edges
        cost = 0
        connected_edges = 0

        # Iterate through the sorted edges and built the minimum spanning tree
        for edge in edges:
            u, v, weight = edge
            if find(parent, u) != find(parent, v):
                # If the endpoints are in different connected components,
                # add the edge and merge the components
                union(parent, u, v)
                cost += weight
                connected_edges += 1
                if connected_edges == n - 1:
                    break

        # The final cost is the minimum to connect all points
        return cost
