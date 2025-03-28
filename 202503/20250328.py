# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
import bisect
import heapq


class Solution:
    """2503. Maximum Number of Points From Grid Queries

    You are given an `m x n` integer matrix `grid` and an array `queries` of size `k`.

    Find an array `answer` of size `k` such that for each integer `queries[i]` you start
    in the **top left** cell of the matrix and repeat the following process:

    * If `queries[i]` is **strictly** greater than the value of the current cell that
    you are in, then you get one point if it is your first time visiting this cell, and
    you can move to any **adjacent** cell in all `4` directions: up, down, left, and
    right.

    * Otherwise, you do not get any points, and you end this process.

    After the process, `answer[i]` is the **maximum** number of points you can get.
    **Note** that for each query you are allowed to visit the same cell **multiple**
    times.

    Return *the resulting array* `answer`."""

    def max_points(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        m, n = len(grid), len(grid[0])
        
        # Initialize distance matrix
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = grid[0][0]
        
        # Priority queue: (dist, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        
        # Dijkstra's algorithm
        while heap:
            dist, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            # Explore adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_dist = max(dist, grid[nr][nc])
                    if new_dist < distance[nr][nc]:
                        distance[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))
        
        # Collect and sort all distances
        all_distances = sorted(distance[r][c] for r in range(m) for c in range(n))
        
        # Process each query
        answer = []
        for q in queries:
            count = bisect.bisect_left(all_distances, q)
            answer.append(count)
        
        return answer

    maxPoints = max_points
