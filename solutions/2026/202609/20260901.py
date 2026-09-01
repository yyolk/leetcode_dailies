# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/


class Solution:
    """3568. Minimum Moves to Clean the Classroom

    You are given an `m x n` grid `classroom` where a student volunteer is tasked with
    cleaning up litter scattered around the room. Each cell in the grid is one of the
    following:

    * `'S'`: Starting position of the student

    * `'L'`: Litter that must be collected (once collected, the cell becomes empty)

    * `'R'`: Reset area that restores the student's energy to full capacity, regardless
    of their current energy level (can be used multiple times)

    * `'X'`: Obstacle the student cannot pass through

    * `'.'`: Empty space

    You are also given an integer `energy`, representing the student's maximum energy
    capacity. The student starts with this energy from the starting position `'S'`.

    Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If
    the energy reaches 0, the student can only continue if they are on a reset area
    `'R'`, which resets the energy to its **maximum** capacity `energy`.

    Return the **minimum** number of moves required to collect all litter items, or `-1`
    if it's impossible.

    Constraints:

    * `1 <= m == classroom.length <= 20`

    * `1 <= n == classroom[i].length <= 20`

    * `classroom[i][j]` is one of `'S'`, `'L'`, `'R'`, `'X'`, or `'.'`

    * `1 <= energy <= 50`

    * There is exactly **one** `'S'` in the grid.

    * There are **at most** 10 `'L'` cells in the grid.
    """

    def min_moves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        # Map each litter cell to a unique bit index.
        litter_id = [[0] * n for _ in range(m)]
        start_r = start_c = 0
        litter_count = 0
        for i, row in enumerate(classroom):
            for j, cell in enumerate(row):
                if cell == "S":
                    start_r, start_c = i, j
                elif cell == "L":
                    litter_id[i][j] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1
        # visited[r][c][e][mask] — True if this state has been seen.
        visited = [
            [
                [[False] * (1 << litter_count) for _ in range(energy + 1)]
                for _ in range(n)
            ]
            for _ in range(m)
        ]
        # BFS state: (row, col, remaining_energy, remaining_litter_mask)
        # Mask starts full; bits are cleared as litters are collected.
        queue = [(start_r, start_c, energy, full_mask)]
        visited[start_r][start_c][energy][full_mask] = True
        dirs = (-1, 0, 1, 0, -1)
        moves = 0

        while queue:
            next_queue = []
            for r, c, cur_energy, mask in queue:
                if mask == 0:
                    return moves
                # Cannot leave a cell that has zero energy left.
                if cur_energy <= 0:
                    continue
                for k in range(4):
                    nr, nc = r + dirs[k], c + dirs[k + 1]
                    if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                        # Reset energy fully when stepping on an R cell.
                        nxt_energy = (
                            energy if classroom[nr][nc] == "R" else cur_energy - 1
                        )
                        nxt_mask = mask
                        if classroom[nr][nc] == "L":
                            # Clear the bit corresponding to this litter.
                            nxt_mask &= ~(1 << litter_id[nr][nc])
                        if not visited[nr][nc][nxt_energy][nxt_mask]:
                            visited[nr][nc][nxt_energy][nxt_mask] = True
                            next_queue.append((nr, nc, nxt_energy, nxt_mask))
            queue = next_queue
            moves += 1

        return -1

    minMoves = min_moves
