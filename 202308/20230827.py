class Solution:
    """403. Frog Jump

    A frog is crossing a river.
    The river is divided into some number of units, and at each unit,
    there may or may not exist a stone. The frog can jump on a stone,
    but it must not jump into the water.

    Given a list of `stones`' positions (in units) in sorted ascending
    order, determine if the frog can cross the river by landing on the
    last stone. Initially, the frog is on the first stone and assumes
    the first jump must be `1` unit.

    If the frog's last jump was `k` units, its next jump must be either
    `k - 1`, `k`, or `k + 1` units.
    The frog can only jump in the forward direction.
    """
    def canCross(self, stones: List[int]) -> bool:
        """Can the frug jump?

        Args:
            stones (List of int): A list of `stones`' positions in sorted,
                ascending order.

        Returns:
            bool: Whether the frog can jump across the river.
        """
        # A dictionary to store valid jump sizes for each stone
        dp = {stone: set() for stone in stones}
        dp[0].add(0)  # Init the first stone with a jump of 0
        
        for stone in stones:
            for jump in dp[stone]:
                # Check the next possible positions that can be reached from the current stone
                for next_jump in range(jump - 1, jump + 2):
                    if next_jump > 0 and stone + next_jump in dp:
                        dp[stone + next_jump].add(next_jump)

        # If the last stone has any valid jump sizes, the frog can cross the river
        return len(dp[stones[-1]]) > 0