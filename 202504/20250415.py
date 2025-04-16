# https://leetcode.com/problems/count-good-triplets-in-an-array/


class FenwickTree:
    def __init__(self, size):
        self.size = size
        # 1-based indexing
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        """Update the tree by adding value at index (1-based)."""
        while index <= self.size:
            self.tree[index] += value
            # Move to next relevant index
            index += index & -index

    def query(self, index):
        """Compute prefix sum from index 1 to index (1-based)."""
        total = 0
        while index > 0:
            total += self.tree[index]
            # Move to parent index
            index -= index & -index
        return total


class Solution:
    """2179. Count Good Triplets in an Array

    You are given two **0-indexed** arrays `nums1` and `nums2` of length `n`, both of
    which are **permutations** of `[0, 1, ..., n - 1]`.

    A **good triplet** is a set of `3` **distinct** values which are present in
    **increasing order** by position both in `nums1` and `nums2`. In other words, if we
    consider `pos1v` as the index of the value `v` in `nums1` and `pos2v` as the index
    of the value `v` in `nums2`, then a good triplet will be a set `(x, y, z)` where `0
    <= x, y, z <= n - 1`, such that `pos1x < pos1y < pos1z` and `pos2x < pos2y < pos2z`.

    Return *the **total number** of good triplets*."""

    def good_triplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        # Step 1: Create position array for nums2
        pos2 = [0] * n
        for i in range(n):
            # pos2[v] = index of value v in nums2
            pos2[nums2[i]] = i

        # Step 2: Left pass to count elements x before y in both arrays
        ft = FenwickTree(n)
        left_count = [0] * n
        for i in range(n):
            y = nums1[i]
            # Number of x with pos2[x] < pos2[y] among elements seen (pos1[x] < i)
            # Sum up to pos2[y]
            left_count[i] = ft.query(pos2[y] + 1)
            # Add y to the tree
            ft.update(pos2[y] + 1, 1)

        # Step 3: Right pass to count elements z after y in both arrays
        ft2 = FenwickTree(n)
        right_count = [0] * n
        for i in range(n - 1, -1, -1):
            y = nums1[i]
            # Number of z with pos2[z] > pos2[y] among elements seen (pos1[z] > i)
            right_count[i] = ft2.query(n) - ft2.query(pos2[y] + 1)
            # Add y to the tree
            ft2.update(pos2[y] + 1, 1)

        # Step 4: Compute total number of good triplets
        total = sum(left_count[i] * right_count[i] for i in range(n))
        return total

    goodTriplets = good_triplets
