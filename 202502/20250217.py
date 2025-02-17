# https://leetcode.com/problems/letter-tile-possibilities/
from collections import Counter


class Solution:
    """1079. Letter Tile Possibilities

    You have `n`  `tiles`, where each tile has one letter `tiles[i]` printed on it.

    Return *the number of possible non-empty sequences of letters* you can make using
    the letters printed on those `tiles`."""

    def num_tile_possibilities(self, tiles: str) -> int:
        # Count the frequency of each character in the tiles
        counter = Counter(tiles)
        
        # Helper function to perform backtracking
        def backtrack(counter):
            count = 0
            for char in counter:
                if counter[char] > 0:
                    # Include this character in the current sequence
                    count += 1
                    counter[char] -= 1
                    # Recursively count the possibilities with the updated counter
                    count += backtrack(counter)
                    # Backtrack: restore the counter for the next iteration
                    counter[char] += 1
            return count
        
        return backtrack(counter)

    numTilePossibilities = num_tile_possibilities
