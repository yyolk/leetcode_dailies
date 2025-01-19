# https://leetcode.com/problems/trapping-rain-water-ii/
import heapq


class Solution:
    """407. Trapping Rain Water II

    Given an `m x n` integer matrix `height_map` representing the height of each unit
    cell in a 2D elevation map, return *the volume of water it can trap after raining*.
    """

    def trap_rain_water(self, height_map: list[list[int]]) -> int:
        if not height_map or not height_map[0]:
            return 0
        
        m, n = len(height_map), len(height_map[0])
        heap = []
        visited = set()
        
        # Add all cells on the border to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (height_map[i][j], i, j))
                    visited.add((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        water_trapped = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    
                    # If the new cell's height is lower, it can trap water up to 'height'
                    if height_map[nx][ny] < height:
                        water_trapped += height - height_map[nx][ny]
                    
                    # Put the new cell into the heap with its height
                    heapq.heappush(heap, (max(height, height_map[nx][ny]), nx, ny))
        
        return water_trapped

    trapRainWater = trap_rain_water
