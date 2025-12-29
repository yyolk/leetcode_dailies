# https://leetcode.com/problems/pyramid-transition-matrix
from collections import defaultdict
from functools import cache


class Solution:
    """756. Pyramid Transition Matrix

    Determine if a pyramid can be built from the given bottom row using only the
    allowed triangular patterns, reaching a single block at the top.
    """
    def pyramid_transition(self, bottom: str, allowed: list[str]) -> bool:
        # Map each pair of bottom blocks to the list of possible top blocks
        next_map = defaultdict(list)
        for pat in allowed:
            next_map[pat[:2]].append(pat[2])

        @cache
        def can_build(row: str) -> bool:
            """Return True if a valid pyramid can be built from this row."""
            if len(row) == 1:
                return True

            # Precompute possible next rows using iterative product
            from itertools import product

            possibilities = []
            n = len(row)
            for i in range(n - 1):
                pair = row[i:i + 2]
                opts = next_map[pair]
                if not opts:  # No way to place a block here
                    return False
                possibilities.append(opts)

            # Generate all possible next rows and check if any works
            for candidate in product(*possibilities):
                next_row = ''.join(candidate)
                if can_build(next_row):
                    return True
            return False

        return can_build(bottom)

    pyramidTransition = pyramid_transition