# https://leetcode.com/problems/tuple-with-same-product/


class Solution:
    """1726. Tuple with Same Product

    Given an array `nums` of **distinct** positive integers, return *the number of
    tuples* `(a, b, c, d)` *such that* `a * b = c * d` *where* `a`*,* `b`*,* `c`*, and*
    `d` *are elements of* `nums`*, and* `a != b != c != d`*.*"""

    def tuple_same_product(self, nums: list[int]) -> int:
        product_count = {}
        
        # Generate all possible products of pairs
        for a, b in combinations(nums, 2):
            product = a * b
            if product in product_count:
                product_count[product] += 1
            else:
                product_count[product] = 1
        
        total = 0
        
        # Calculate the number of valid tuples for each product
        for count in product_count.values():
            if count >= 2:
                total += comb(count, 2) * 8
        
        return total

    tupleSameProduct = tuple_same_product
