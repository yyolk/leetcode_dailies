# https://leetcode.com/problems/stone-game-viii/


class Solution:
    """1872. Stone Game VIII

    Alice and Bob take turns playing a game, with **Alice starting first**.

    There are `n` stones arranged in a row. On each player's turn, while the number of
    stones is **more than one**, they will do the following:

    1. Choose an integer `x > 1`, and **remove** the leftmost `x` stones from the row.

    2. Add the **sum** of the **removed** stones' values to the player's score.

    3. Place a **new stone**, whose value is equal to that sum, on the left side of the
    row.

    The game stops when **only** **one** stone is left in the row.

    The **score difference** between Alice and Bob is `(Alice's score - Bob's score)`.
    Alice's goal is to **maximize** the score difference, and Bob's goal is the
    **minimize** the score difference.

    Given an integer array `stones` of length `n` where `stones[i]` represents the value
    of the `ith` stone **from the left**, return *the **score difference** between Alice
    and Bob if they both play **optimally**.*

    Constraints:

    * `n == stones.length`

    * `2 <= n <= 105`

    * `-104 <= stones[i] <= 104`"""

    def stone_game_v_i_i_i(self, stones: list[int]) -> int:
        """Return the optimal score difference (Alice - Bob)."""
        prefix_sum = 0
        prefix_sums: list[int] = []
        for stone in stones:
            prefix_sum += stone
            prefix_sums.append(prefix_sum)

        best = prefix_sums[-1]
        for i in range(len(stones) - 2, 0, -1):
            best = max(best, prefix_sums[i] - best)

        return best

    stoneGameVIII = stone_game_v_i_i_i
