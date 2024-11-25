# https://leetcode.com/problems/sliding-puzzle/


class Solution:
    """773. Sliding Puzzle

    On an `2 x 3` board, there are five tiles labeled from `1` to `5`, and an empty
    square represented by `0`. A **move** consists of choosing `0` and a 4-directionally
    adjacent number and swapping it.

    The state of the board is solved if and only if the board is `[[1,2,3],[4,5,0]]`.

    Given the puzzle board `board`, return *the least number of moves required so that
    the state of the board is solved*. If it is impossible for the state of the board to
    be solved, return `-1`."""

    def sliding_puzzle(self, board: list[list[int]]) -> int:
        # Convert board to string representation
        start = "".join(str(num) for row in board for num in row)
        target = "123450"  # Solved state

        # Define valid moves for each position of "0"
        neighbors = {
            0: (1, 3), 1: (0, 2, 4), 2: (1, 5),
            3: (0, 4), 4: (1, 3, 5), 5: (2, 4)
        }

        def swap(s, i, j):
            """Helper function to swap two characters in a string."""
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        visited = set()
        queue = deque([(start, 0)])

        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves

            if state in visited:
                continue

            visited.add(state)
            zero_pos = state.index("0")
            for neighbor in neighbors[zero_pos]:
                new_state = swap(state, zero_pos, neighbor)
                if new_state not in visited:
                    queue.append((new_state, moves + 1))

        # If no solution found
        return -1

    slidingPuzzle = sliding_puzzle
