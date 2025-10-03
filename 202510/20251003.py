# https://leetcode.com/problems/trapping-rain-water-ii/
import heapq


class Solution:
    """407. Trapping Rain Water II

    Given an `m x n` integer matrix `height_map` representing the height of each unit
    cell in a 2D elevation map, return *the volume of water it can trap after raining*.
    """

    def trap_rain_water(self, height_map: list[list[int]]) -> int:
        # Handle empty map cases
        if not height_map or not height_map[0]:
            return 0
        
        # Get dimensions
        m, n = len(height_map), len(height_map[0])
        
        # Min-heap for cells, prioritized by height
        heap = []
        
        # Visited matrix to track processed cells
        visited = [[False] * n for _ in range(m)]
        
        # Add left and right boundary cells to heap
        for i in range(m):
            heapq.heappush(heap, (height_map[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(heap, (height_map[i][n-1], i, n-1))
            visited[i][n-1] = True
        
        # Add top and bottom boundary cells to heap, avoiding corners duplication
        for j in range(1, n-1):
            heapq.heappush(heap, (height_map[0][j], 0, j))
            visited[0][j] = True
            heapq.heappush(heap, (height_map[m-1][j], m-1, j))
            visited[m-1][j] = True
        
        # Total trapped water
        total = 0
        
        # Directions for neighbors: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Process heap until empty
        while heap:
            # Pop cell with smallest height (bottleneck)
            h, i, j = heapq.heappop(heap)
            
            # Check each neighbor
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                
                # If neighbor is valid and not visited
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    
                    # Calculate trapped water at neighbor: max(0, incoming bottleneck - neighbor height)
                    total += max(0, h - height_map[ni][nj])
                    
                    # Push neighbor with updated bottleneck: max(incoming bottleneck, neighbor height)
                    heapq.heappush(heap, (max(h, height_map[ni][nj]), ni, nj))
        
        return total

    trapRainWater = trap_rain_water
