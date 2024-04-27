# https://leetcode.com/problems/freedom-trail/
from collections import defaultdict
from functools import lru_cache


class Solution:
    """514. Freedom Trail

    In the video game Fallout 4, the quest **"Road to Freedom"** requires players to
    reach a metal dial called the **"Freedom Trail Ring"** and use the dial to spell a
    specific keyword to open the door.

    Given a string `ring` that represents the code engraved on the outer ring and
    another string `key` that represents the keyword that needs to be spelled, return
    *the minimum number of steps to spell all the characters in the keyword*.

    Initially, the first character of the ring is aligned at the `"12:00"` direction.
    You should spell all the characters in `key` one by one by rotating `ring` clockwise
    or anticlockwise to make each character of the string key aligned at the `"12:00"`
    direction and then by pressing the center button.

    At the stage of rotating the ring to spell the key character `key[i]`:

    1. You can rotate the ring clockwise or anticlockwise by one place, which counts as
    **one step**. The final purpose of the rotation is to align one of `ring`'s
    characters at the `"12:00"` direction, where this character must equal `key[i]`.

    2. If the character `key[i]` has been aligned at the `"12:00"` direction, press the
    center button to spell, which also counts as **one step**. After the pressing, you
    could begin to spell the next character in the key (next stage). Otherwise, you have
    finished all the spelling.

    """

    def find_rotate_steps(self, ring: str, key: str) -> int:
        # Length of ring and key, and defaultdict for positions
        r_length, k_length, d = len(ring), len(key), defaultdict(list)
        # Function to calculate distance with circular wrapping
        dist = lambda x, y: min((x - y) % r_length, (y - x) % r_length)

        # Store positions of characters in the ring
        for i, ch in enumerate(ring):
            d[ch].append(i)

        # Memoize results to avoid redundant computations
        @lru_cache(None)
        def dfs(curr=0, next=0):
            # Base case: all characters in key have been spelled
            if next >= k_length:
                return 0

            # Recursive call to explore all possible paths
            return min(dist(curr, k) + dfs(k, next + 1) for k in d[key[next]])

        # Add length of key to account for pressing center button after spelling
        return dfs() + k_length

    findRotateSteps = find_rotate_steps
