# https://leetcode.com/problems/longest-balanced-subarray-ii

class SegmentTree:
    def __init__(self, N: int):
        # Next power of 2 covering 0 to N-1 (N = len(nums) + 1)
        self.base = 1 << (N - 1).bit_length() if N > 1 else 1
        self.lazy = [0] * (2 * self.base)
        self.minv = [0] * (2 * self.base)
        self.maxv = [0] * (2 * self.base)

    def apply(self, x: int, val: int) -> None:
        # Add val to min/max at node x
        self.minv[x] += val
        self.maxv[x] += val
        # Propagate to lazy if not leaf
        if x < self.base:
            self.lazy[x] += val

    def pull(self, x: int) -> None:
        # Update ancestors' min/max, accounting for lazy
        while x > 1:
            x //= 2
            self.minv[x] = min(self.minv[2 * x], self.minv[2 * x + 1])
            self.maxv[x] = max(self.maxv[2 * x], self.maxv[2 * x + 1])
            if self.lazy[x]:
                self.minv[x] += self.lazy[x]
                self.maxv[x] += self.lazy[x]

    def update(self, L: int, R: int, val: int) -> None:
        # Range add val on [L, R] (inclusive, 0-based shifted by base)
        L += self.base
        R += self.base
        L0, R0 = L, R
        while L <= R:
            if L % 2 == 1:
                self.apply(L, val)
                L += 1
            if R % 2 == 0:
                self.apply(R, val)
                R -= 1
            L //= 2
            R //= 2
        self.pull(L0)
        self.pull(R0)

    def binary_search(self, x: int) -> int:
        # Find leftmost index with value == x (prefers left, pushes lazy)
        i = 1
        while i < self.base:
            if self.lazy[i]:
                self.apply(2 * i, self.lazy[i])
                self.apply(2 * i + 1, self.lazy[i])
                self.lazy[i] = 0
            i *= 2  # Try left child
            if not (self.minv[i] <= x <= self.maxv[i]):
                i += 1  # Go right if left cannot contain x
        return i - self.base


class Solution:
    """3721. Longest Balanced Subarray II
    
    You are given an integer array nums.
    A subarray is called balanced if the number of distinct even numbers
    in the subarray is equal to the number of distinct odd numbers.
    Return the length of the longest balanced subarray.
    """
    def longest_balanced(self, nums: list[int]) -> int:
        n = len(nums)
        # Virtual position 0 has balance 0
        st = SegmentTree(n + 1)
        # Last seen position of each number
        lookup = {}
        # Current balance: distinct odds - distinct evens in prefix [1..i]
        curr = 0
        ans = 0
        for i in range(1, n + 1):
            num = nums[i - 1]
            # +1 for odd, -1 for even
            d = 1 if num & 1 else -1
            # If repeat, cancel contribution from previous last position
            if num in lookup:
                prev = lookup[num]
                st.update(prev, n, -d)
                curr -= d
            # Add contribution at current position
            curr += d
            lookup[num] = i
            st.update(i, n, d)
            # Leftmost position with same balance as curr
            left = st.binary_search(curr)
            # Subarray from left+1 to i has balance 0 (equal distinct counts)
            ans = max(ans, i - left)
        return ans

    longestBalanced = longest_balanced