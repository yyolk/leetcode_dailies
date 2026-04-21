# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

from collections import defaultdict, Counter

class Solution:
    """1722. Minimize Hamming Distance After Swap Operations
    
    You are given two integer arrays, source and target, both of length n. You are
    also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi]
    indicates that you are allowed to swap the elements at index ai and index bi
    (0-indexed) of array source. Note that you can swap elements at a specific
    pair of indices multiple times and in any order.
    
    The Hamming distance of two arrays of the same length, source and target, is
    the number of positions where the elements are different. Formally, it is the
    number of indices i for 0 <= i <= n-1 where source[i] != target[i]
    (0-indexed).
    
    Return the minimum Hamming distance of source and target after performing any
    amount of swap operations on array source.
    """
    def minimum_hamming_distance(self, source: list[int], target: list[int], allowed_swaps: list[list[int]]) -> int:
        n = len(source)
        # Union-Find parent array for indices 0 to n-1
        parent = list(range(n))
        def find(x: int) -> int:
            if parent[x] != x:
                # path compression for amortized O(1) finds
                parent[x] = find(parent[x])
            return parent[x]
        def union(x: int, y: int) -> None:
            px = find(x)
            py = find(y)
            if px != py:
                # simple union (no rank needed for speed here)
                parent[px] = py
        # connect all swappable index pairs into components
        for a, b in allowed_swaps:
            union(a, b)
        # group indices belonging to each connected component
        components = defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
        total_matches = 0
        for comp in components.values():
            # frequency of each value available in source for this component
            source_count = Counter(source[i] for i in comp)
            # frequency of each desired value in target for this component
            target_count = Counter(target[i] for i in comp)
            # max positions that can be matched in component
            matches = sum(min(source_count[v], target_count[v]) for v in source_count)
            total_matches += matches
        # minimum Hamming distance is unmatched positions across all n indices
        return n - total_matches

    minimumHammingDistance = minimum_hamming_distance