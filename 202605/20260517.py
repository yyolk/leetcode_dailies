# https://leetcode.com/problems/jump-game-iii/

from collections import deque


class Solution:
    """1306. Jump Game III
    
    Given an array of non-negative integers arr, you are initially positioned at
    start index of the array. When you are at index i, you can jump to i + arr[i]
    or i - arr[i], check if you can reach any index with value 0. Notice that you
    can not jump outside of the array at any time.
    """
    def can_reach(self, arr: list[int], start: int) -> bool:
        # BFS for reachability from start position
        n = len(arr)
        # visited array to prevent revisiting positions and cycles
        visited = [False] * n
        queue = deque([start])
        visited[start] = True
        
        while queue:
            i = queue.popleft()
            # check if current position has zero
            if arr[i] == 0:
                return True
            # try both possible jumps: +arr[i] and -arr[i]
            for delta in (arr[i], -arr[i]):
                j = i + delta
                # validate bounds and not visited
                if 0 <= j < n and not visited[j]:
                    visited[j] = True
                    queue.append(j)
        return False

    canReach = can_reach