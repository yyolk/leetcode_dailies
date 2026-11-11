# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/


class Solution:
    """3789. Minimum Cost to Acquire Required Items

    You are given five integers `cost1`, `cost2`, `cost_both`, `need1`, and `need2`.

    There are three types of items available:

    * An item of **type 1** costs `cost1` and contributes 1 unit to the type 1
    requirement only.

    * An item of **type 2** costs `cost2` and contributes 1 unit to the type 2
    requirement only.

    * An item of **type 3** costs `cost_both` and contributes 1 unit to **both** type 1
    and type 2 requirements.

    You must collect enough items so that the total contribution toward type 1 is **at
    least** `need1` and the total contribution toward type 2 is **at least** `need2`.

    Return an integer representing the **minimum** possible total cost to achieve these
    requirements.

    Constraints:

    * `1 <= cost1, cost2, cost_both <= 106`

    * `0 <= need1, need2 <= 109`"""

    def minimum_cost(
        self, cost1: int, cost2: int, cost_both: int, need1: int, need2: int
    ) -> int:
        """...

        Proposed solution ...

        Args:
            cost1 (int): ...
            cost2 (int): ...
            cost_both (int): ...
            need1 (int): ...
            need2 (int): ...

        Returns:
            int: ..."""
        ...

    minimumCost = minimum_cost
