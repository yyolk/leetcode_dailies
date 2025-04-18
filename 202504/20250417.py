# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/


class Solution:
    """2176. Count Equal and Divisible Pairs in an Array

    Given a **0-indexed** integer array `nums` of length `n` and an integer `k`, return
    *the **number of pairs*** `(i, j)` *where* `0 <= i < j < n`, *such that* `nums[i] ==
    nums[j]` *and* `(i * j)` *is divisible by* `k`."""

    def count_pairs(self, nums: list[int], k: int) -> int:
        # Step 1: Group indices by value using a defaultdict
        index_dict = defaultdict(list)
        for i, num in enumerate(nums):
            index_dict[num].append(i)

        # Step 2: Count valid pairs
        count = 0
        for indices in index_dict.values():
            m = len(indices)
            # Generate all pairs (i, j) where i < j
            for i in range(m):
                for j in range(i + 1, m):
                    # Check if the product of indices is divisible by k
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count

    countPairs = count_pairs
