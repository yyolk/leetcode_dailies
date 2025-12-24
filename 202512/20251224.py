# https://leetcode.com/problems/apple-redistribution-into-boxes


class Solution:
    """3074. Apple Redistribution into Boxes

    You are given an array apple of size n and an array capacity of size m.

    There are n packs where the ith pack contains apple[i] apples. There are m
    boxes, and the ith box has a capacity of capacity[i] apples.

    Return the minimum number of boxes needed to redistribute all n packs of
    apples into boxes.

    Note that apples from the same pack can be put into multiple boxes.
    """
    def minimum_boxes(self, apple: list[int], capacity: list[int]) -> int:
        # Total apples that must be stored
        total = sum(apple)
        
        # Sort boxes descending - greedily use largest capacities first
        capacity.sort(reverse=True)
        
        # Accumulate capacity until it meets or exceeds total apples needed
        used = 0
        for i in range(len(capacity)):
            used += capacity[i]
            if used >= total:
                # i+1 boxes are sufficient
                return i + 1
        
        # Edge case: should not reach here if capacity can hold all apples
        return len(capacity)
    
    minimumBoxes = minimum_boxes