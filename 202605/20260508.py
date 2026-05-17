# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

from collections import defaultdict, deque


class Solution:
    """3629. Minimum Jumps to Reach End via Prime Teleportation

    You are given an integer array nums of length n. You start at index 0, and
    your goal is to reach index n - 1. From any index i, you may perform one of
    the following operations: Adjacent Step: Jump to index i + 1 or i - 1, if
    the index is within bounds. Prime Teleportation: If nums[i] is a prime
    number p, you may instantly jump to any index j != i such that nums[j] % p
    == 0. Return the minimum number of jumps required to reach index n - 1.
    """

    def min_jumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # Precompute smallest prime factor (SPF) sieve up to max value in nums
        max_val = max(nums)
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Active primes: only those that appear as nums values
        possible_ps = {x for x in nums if x >= 2 and spf[x] == x}

        # Teleport targets: p -> list of indices j where p divides nums[j]
        # Factorize each nums[j] using SPF (O(log nums[j]) per element)
        tele = defaultdict(list)
        for j in range(n):
            val = nums[j]
            if val < 2:
                continue
            x = val
            while x > 1:
                p = spf[x]
                if p in possible_ps:
                    tele[p].append(j)
                while x % p == 0:
                    x //= p

        # BFS for minimum jumps (unit cost edges)
        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])
        while queue:
            i = queue.popleft()
            if i == n - 1:
                return dist[i]
            d = dist[i]

            # Adjacent steps (always available)
            for di in (-1, 1):
                ni = i + di
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = d + 1
                    queue.append(ni)

            # Prime teleportation (process each prime only once via delete)
            p = nums[i]
            if p in tele:
                for j in tele[p]:
                    if dist[j] == -1:
                        dist[j] = d + 1
                        queue.append(j)
                del tele[p]

        return -1  # Always reachable via adjacent steps

    minJumps = min_jumps
