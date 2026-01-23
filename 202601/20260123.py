# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii
import heapq


class Solution:
    """3510. Minimum Pair Removal to Sort Array II

    Given an array nums, you can perform the following operation any number of
    times:

    Select the adjacent pair with the minimum sum in nums. If multiple such
    pairs exist, choose the leftmost one.
    Replace the pair with their sum.
    Return the minimum number of operations needed to make the array
    non-decreasing.

    An array is said to be non-decreasing if each element is greater than or
    equal to its previous element (if it exists).
    """

    class Node:
        def __init__(self, val: int, pos: int):
            # Node represents a segment with its sum value and leftmost position
            self.val = val
            self.pos = pos
            self.prev = None
            self.next = None
            self.active = True

    def minimum_pair_removal(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Build doubly linked list of nodes
        nodes = [self.Node(nums[i], i) for i in range(n)]
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        head = nodes[0]

        # Initialize min-heap for adjacent sums: (sum, pos, counter, left_node)
        heap = []
        cnt = 0
        for i in range(n - 1):
            s = nodes[i].val + nodes[i + 1].val
            heapq.heappush(heap, (s, nodes[i].pos, cnt, nodes[i]))
            cnt += 1

        # Count initial violations (places where next < current)
        violations = 0
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                violations += 1
            cur = cur.next

        if violations == 0:
            return 0

        # Simulate merges until no violations
        ops = 0
        while violations > 0:
            # Find the valid min sum pair
            while heap:
                s, p, c, left = heapq.heappop(heap)
                if not left.active or not left.next or not left.next.active:
                    continue
                right = left.next
                curr_s = left.val + right.val
                if curr_s != s:
                    continue
                # Valid pair found
                break
            else:
                # No pairs left, should not happen
                return -1  # Error case

            # Create new node with sum
            new_val = left.val + right.val
            new_pos = left.pos
            new_node = self.Node(new_val, new_pos)

            prevv = left.prev
            nextt = right.next

            # Update violation count
            # Remove violation from merged pair if existed
            if right.val < left.val:
                violations -= 1
            # Update left side violation
            if prevv:
                old_vio = left.val < prevv.val
                new_vio = new_val < prevv.val
                if old_vio:
                    violations -= 1
                if new_vio:
                    violations += 1
            # Update right side violation
            if nextt:
                old_vio = nextt.val < right.val
                new_vio = nextt.val < new_val
                if old_vio:
                    violations -= 1
                if new_vio:
                    violations += 1

            # Link new node in the list
            new_node.prev = prevv
            new_node.next = nextt
            if prevv:
                prevv.next = new_node
            if nextt:
                nextt.prev = new_node

            # Deactivate old nodes
            left.active = False
            right.active = False

            # Add new adjacent pairs to heap
            if prevv:
                s_new = prevv.val + new_val
                heapq.heappush(heap, (s_new, prevv.pos, cnt, prevv))
                cnt += 1
            if nextt:
                s_new = new_val + nextt.val
                heapq.heappush(heap, (s_new, new_pos, cnt, new_node))
                cnt += 1

            # Increment operation count
            ops += 1

        return ops

    minimumPairRemoval = minimum_pair_removal