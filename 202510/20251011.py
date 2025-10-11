# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
from collections import Counter
import bisect


class Solution:
    """3186. Maximum Total Damage With Spell Casting

    A magician has various spells.

    You are given an array `power`, where each element represents the damage of a spell.
    Multiple spells can have the same damage value.

    It is a known fact that if a magician decides to cast a spell with a damage of
    `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`,
    `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

    Each spell can be cast **only once**.

    Return the **maximum** possible *total damage* that a magician can cast."""

    def maximum_total_damage(self, power: list[int]) -> int:
        # Count frequency of each damage value
        freq = Counter(power)
        if not freq:
            return 0
        # Sort unique damage values
        ds = sorted(freq.keys())
        k = len(ds)
        # Precompute value for each unique damage: damage * frequency
        val = [ds[i] * freq[ds[i]] for i in range(k)]
        # dp[i] will be the max damage using the first i unique damages
        dp = [0] * (k + 1)
        for i in range(1, k + 1):
            # Option 1: Skip the current damage, take previous max
            max_sum = dp[i - 1]
            # Find the position p: number of damages <= ds[i-1] - 3
            target = ds[i - 1] - 3
            p = bisect.bisect_right(ds, target)
            # Option 2: Take current, add to max from damages up to p (those <= ds[i-1] - 3)
            take = val[i - 1] + dp[p]
            # Update dp[i] with the better option
            dp[i] = max(max_sum, take)
        return dp[k]

    maximumTotalDamage = maximum_total_damage
