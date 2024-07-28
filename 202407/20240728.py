# https://leetcode.com/problems/second-minimum-time-to-reach-destination/


class Solution:
    """2045. Second Minimum Time to Reach Destination

    A city is represented as a **bi\\-directional connected** graph with `n` vertices
    where each vertex is labeled from `1` to `n` (**inclusive**). The edges in the graph
    are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]`
    denotes a bi\\-directional edge between vertex `ui` and vertex `vi`. Every vertex
    pair is connected by **at most one** edge, and no vertex has an edge to itself. The
    time taken to traverse any edge is `time` minutes.

    Each vertex has a traffic signal which changes its color from **green** to **red**
    and vice versa every `change` minutes. All signals change **at the same time**. You
    can enter a vertex at **any time**, but can leave a vertex **only when the signal is
    green**. You **cannot wait** at a vertex if the signal is **green**.

    The **second minimum value** is defined as the smallest value **strictly larger**
    than the minimum value.

    * For example the second minimum value of `[2, 3, 4]` is `3`, and the second minimum
    value of `[2, 2, 4]` is `4`.

    Given `n`, `edges`, `time`, and `change`, return *the **second minimum time** it
    will take to go from vertex* `1` *to vertex* `n`.

    **Notes:**

    * You can go through any vertex **any** number of times, **including** `1` and `n`.

    * You can assume that when the journey **starts**, all signals have just turned
    **green**.

    """

    def second_minimum(
        self, n: int, edges: list[list[int]], time: int, change: int
    ) -> int:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize distances to store the minimum and second minimum times
        dist = [[float('inf'), float('inf')] for _ in range(n + 1)]
        dist[1][0] = 0  # Starting point (node 1) with 0 time

        # BFS queue (node, current time)
        queue = deque([(1, 0)])
        
        while queue:
            node, current_time = queue.popleft()
            
            # Determine current cycle time (whether red or green)
            cycle = current_time // change
            if cycle % 2 == 1:  # If it's a red signal
                current_time = (cycle + 1) * change  # Wait for green signal
            
            # Explore neighbors
            for neighbor in graph[node]:
                new_time = current_time + time
                if new_time < dist[neighbor][0]:
                    dist[neighbor][1] = dist[neighbor][0]
                    dist[neighbor][0] = new_time
                    queue.append((neighbor, new_time))
                elif dist[neighbor][0] < new_time < dist[neighbor][1]:
                    dist[neighbor][1] = new_time
                    queue.append((neighbor, new_time))

        return dist[n][1]

    secondMinimum = second_minimum
