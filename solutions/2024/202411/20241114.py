# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/


class Solution:
    """2064. Minimized Maximum of Products Distributed to Any Store

    You are given an integer `n` indicating there are `n` specialty retail stores. There
    are `m` product types of varying amounts, which are given as a **0\\-indexed**
    integer array `quantities`, where `quantities[i]` represents the number of products
    of the `ith` product type.

    You need to distribute **all products** to the retail stores following these rules:

    * A store can only be given **at most one product type** but can be given **any**
    amount of it.

    * After distribution, each store will have been given some number of products
    (possibly `0`). Let `x` represent the maximum number of products given to any store.
    You want `x` to be as small as possible, i.e., you want to **minimize** the
    **maximum** number of products that are given to any store.

    Return *the minimum possible* `x`.

    """

    def minimized_maximum(self, n: int, quantities: list[int]) -> int:
        def can_distribute(x: int) -> bool:
            # Check if it's possible to distribute products so that no store gets more than x items
            stores_needed = sum((q + x - 1) // x for q in quantities)
            return stores_needed <= n

        # Binary search for the minimum maximized value
        # right could be any product quantity
        left, right = 1, max(quantities)

        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left

    minimizedMaximum = minimized_maximum
