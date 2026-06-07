# https://leetcode.com/problems/jump-game-iv/

from collections import deque


class Solution:
    """1345. Jump Game IV

    Given an array of integers arr, you are initially positioned at the first index of
    the array. In one step you can jump from index i to index:
    * i + 1 where: i + 1 < arr.length.
    * i - 1 where: i - 1 >= 0.
    * j where: arr[i] == arr[j] and i != j.
    Return the minimum number of steps to reach the last index of the array.
    Notice that you can not jump outside of the array at any time.
    """

    def min_jumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # Build map: value -> list of indices for efficient same-value jumps
        val_to_idx = {}
        for i in range(n):
            val_to_idx.setdefault(arr[i], []).append(i)

        # BFS for min steps: queue holds indices
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0

        while queue:
            # Process entire level for current step count
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == n - 1:
                    return steps

                # Adjacent jumps to curr-1 and curr+1
                for nxt in (curr - 1, curr + 1):
                    if 0 <= nxt < n and not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)

                # Same-value jumps: all indices with arr[curr]
                # pop to ensure group processed only once for O(n) total time
                if arr[curr] in val_to_idx:
                    indices = val_to_idx.pop(arr[curr])
                    for j in indices:
                        if not visited[j]:
                            visited[j] = True
                            queue.append(j)
            steps += 1

        return -1  # Unreachable as end is always accessible

    minJumps = min_jumps
