# https://leetcode.com/problems/number-of-paths-with-max-score/

class Solution:
    """1301. Number of Paths with Max Score

    You are given a square board of characters. You can move starting at bottom
    right 'S' to reach top left 'E'. The rest are labeled 1-9 or obstacle 'X'. In
    one move go up, left or up-left (diagonal) only if no obstacle. Return [max
    sum of numeric characters collectible, number of such paths mod 10^9+7]. If
    no path return [0, 0].
    """

    def paths_with_max_score(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        # max from each cell incl its val; -1 means unreachable to E
        max_dp = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]
        # base E at [0][0]: val 0 (not digit), 1 way
        max_dp[0][0] = 0
        ways[0][0] = 1
        for r in range(n):
            for c in range(n):
                # skip E and obstacles (already handled)
                if (r == 0 and c == 0) or board[r][c] == "X":
                    continue
                # current cell contrib (0 for S/E)
                v = int(board[r][c]) if board[r][c].isdigit() else 0
                max_next = -1
                cnt = 0
                # check 3 possible next (toward E: smaller idx)
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if nr >= 0 and nc >= 0 and max_dp[nr][nc] != -1:
                        nxt = max_dp[nr][nc]
                        if nxt > max_next:
                            max_next = nxt
                            cnt = ways[nr][nc]
                        elif nxt == max_next:
                            cnt = (cnt + ways[nr][nc]) % MOD
                # update only if reachable continuation exists
                if max_next != -1:
                    max_dp[r][c] = v + max_next
                    ways[r][c] = cnt
        # extract from S at bottom-right
        sr = sc = n - 1
        if max_dp[sr][sc] == -1:
            return [0, 0]
        return [max_dp[sr][sc], ways[sr][sc]]

    pathsWithMaxScore = paths_with_max_score
