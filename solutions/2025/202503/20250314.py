# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/


class Solution:
    """2226. Maximum Candies Allocated to K Children

    You are given a **0-indexed** integer array `candies`. Each element in the array
    denotes a pile of candies of size `candies[i]`. You can divide each pile into any
    number of **sub piles**, but you **cannot** merge two piles together.

    You are also given an integer `k`. You should allocate piles of candies to `k`
    children such that each child gets the **same** number of candies. Each child can be
    allocated candies from **only one** pile of candies and some piles of candies may go
    unused.

    Return *the **maximum number of candies** each child can get.*"""

    def maximum_candies(self, candies: list[int], k: int) -> int:
        # Calculate the total number of candies available
        total_candies = sum(candies)

        # If total candies are less than k, it's impossible to give each child at least one candy
        if total_candies < k:
            return 0

        # Define a helper function to check if a certain number of candies per child is possible
        def can_allocate(max_candies):
            # Calculate how many children can be given max_candies from the piles
            return sum(candy // max_candies for candy in candies) >= k

        # Initialize binary search bounds:
        # - left: minimum possible candies per child (1)
        # - right: maximum possible candies per child (total_candies // k)
        left, right = 1, total_candies // k

        # Perform binary search to find the maximum possible candies per child
        while left < right:
            # Calculate the midpoint, biased towards the higher end
            mid = (left + right) // 2 + 1
            # If it's possible to allocate mid candies to at least k children, search higher
            if can_allocate(mid):
                left = mid
            # Otherwise, search lower
            else:
                right = mid - 1

        # After the loop, left is the maximum number of candies that can be allocated to each of k children
        return left

    maximumCandies = maximum_candies
