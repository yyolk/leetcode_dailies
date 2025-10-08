# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/


class Solution:
    """2300. Successful Pairs of Spells and Potions

    You are given two positive integer arrays `spells` and `potions`, of length `n` and
    `m` respectively, where `spells[i]` represents the strength of the `ith` spell and
    `potions[j]` represents the strength of the `jth` potion.

    You are also given an integer `success`. A spell and potion pair is considered
    **successful** if the **product** of their strengths is **at least** `success`.

    Return *an integer array* `pairs` *of length* `n` *where* `pairs[i]` *is the number
    of **potions** that will form a successful pair with the* `ith` *spell.*"""

    def successful_pairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        # Sort potions in ascending order to enable binary search
        potions.sort()
        
        # Helper function: binary search to find leftmost index where arr[idx] >= target
        def binary_search(arr: list[int], target: int) -> int:
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # Initialize result list
        result = []
        
        # For each spell, compute required potion strength and count successful pairs
        for spell in spells:
            # Compute ceiling of success / spell using integer arithmetic
            required = (success + spell - 1) // spell
            # Find starting index of potions >= required
            idx = binary_search(potions, required)
            # Count potions from idx to end
            count = len(potions) - idx
            result.append(count)
        
        return result

    successfulPairs = successful_pairs
