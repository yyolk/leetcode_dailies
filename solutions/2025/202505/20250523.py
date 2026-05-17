# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/


class Solution:
    """3068. Find the Maximum Sum of Node Values

    There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are
    given a **0-indexed** 2D integer array `edges` of length `n - 1`, where `edges[i] =
    [ui, vi]` indicates that there is an edge between nodes `ui` and `vi` in the tree.
    You are also given a **positive** integer `k`, and a **0-indexed** array of **non-
    negative** integers `nums` of length `n`, where `nums[i]` represents the **value**
    of the node numbered `i`.

    Alice wants the sum of values of tree nodes to be **maximum**, for which Alice can
    perform the following operation **any** number of times (**including zero**) on the
    tree:

    * Choose any edge `[u, v]` connecting the nodes `u` and `v`, and update their values
    as follows:

      + `nums[u] = nums[u] XOR k`

      + `nums[v] = nums[v] XOR k`

    Return *the **maximum** possible **sum** of the **values** Alice can achieve by
    performing the operation **any** number of times*."""

    def maximum_value_sum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        # Step 1: Calculate the maximum possible sum
        max_sum = sum(max(num, num ^ k) for num in nums)

        # Step 2: Count nodes where XORing with k increases the value
        changed_count = sum((num ^ k) > num for num in nums)

        # Step 3: If even number of changes, return the max sum
        if changed_count % 2 == 0:
            return max_sum

        # Step 4: If odd, subtract the smallest difference to make changes even
        min_change_diff = min(abs(num - (num ^ k)) for num in nums)
        return max_sum - min_change_diff

    maximumValueSum = maximum_value_sum
