# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
import bisect


class Solution:
    """2106. Maximum Fruits Harvested After at Most K Steps

    Fruits are available at some positions on an infinite x-axis. You are given a 2D
    integer array `fruits` where `fruits[i] = [positioni, amounti]` depicts `amounti`
    fruits at the position `positioni`. `fruits` is already **sorted** by `positioni` in
    **ascending order**, and each `positioni` is **unique**.

    You are also given an integer `start_pos` and an integer `k`. Initially, you are at
    the position `start_pos`. From any position, you can either walk to the **left or
    right**. It takes **one step** to move **one unit** on the x-axis, and you can walk
    **at most** `k` steps in total. For every position you reach, you harvest all the
    fruits at that position, and the fruits will disappear from that position.

    Return *the **maximum total number** of fruits you can harvest*."""

    def max_total_fruits(self, fruits: list[list[int]], start_pos: int, k: int) -> int:
        # Get the number of fruit positions
        n = len(fruits)
        # Extract the positions of the fruits into a list
        pos = [f[0] for f in fruits]
        # Extract the amounts of fruits into a list
        amt = [f[1] for f in fruits]
        # Initialize a prefix sum array with n+1 elements, starting with 0
        prefix = [0] * (n + 1)
        # Loop to compute the prefix sums
        for i in range(n):
            # Update the prefix sum by adding the current amount
            prefix[i + 1] = prefix[i] + amt[i]
        # Find the insertion point for start_pos in pos (leftmost possible index)
        j = bisect.bisect_left(pos, start_pos)
        # Initialize the answer to 0
        ans = 0
        # Check if there's a fruit exactly at start_pos
        if j < n and pos[j] == start_pos:
            # If yes, add its amount to ans
            ans = amt[j]
        # If there are fruits to the left of start_pos
        if j > 0:
            # Find the leftmost position reachable within k steps to the left
            leftmost = bisect.bisect_left(pos, start_pos - k)
            # Ensure leftmost is at least 0
            leftmost = max(leftmost, 0)
            # If there are fruits in this left range
            if leftmost < j:
                # Calculate the sum of fruits from leftmost to j-1
                sum_left = prefix[j] - prefix[leftmost]
                # Update ans if this sum is larger
                ans = max(ans, sum_left)
        # If there are fruits to the right of start_pos
        if j < n:
            # Find the rightmost position reachable within k steps to the right
            rightmost = bisect.bisect_right(pos, start_pos + k) - 1
            # Ensure rightmost is at most n-1
            rightmost = min(rightmost, n - 1)
            # If there are fruits in this right range
            if rightmost >= j:
                # Calculate the sum of fruits from j to rightmost
                sum_right = prefix[rightmost + 1] - prefix[j]
                # Update ans if this sum is larger
                ans = max(ans, sum_right)
        # If there are fruits both left and right
        if j > 0 and j < n:
            # Loop over possible right endpoints starting from j
            for r in range(j, n):
                # Calculate the distance to the right endpoint
                b = pos[r] - start_pos
                # If this distance exceeds k, break the loop
                if b > k:
                    break
                # Initialize max_a to 0 (maximum left distance)
                max_a = 0
                # If k is at least b
                if k >= b:
                    # Check if k is within 3*b
                    if k <= 3 * b:
                        # Calculate max_a as (k - b) // 2
                        max_a = (k - b) // 2
                    else:
                        # Otherwise, max_a = k - 2*b
                        max_a = k - 2 * b
                # Calculate the minimum position on the left
                min_pos_l = start_pos - max_a
                # Find the left index for this min_pos_l
                l = bisect.bisect_left(pos, min_pos_l)
                # If there are fruits to the left
                if l < j:
                    # Calculate the sum from l to r
                    cur_sum = prefix[r + 1] - prefix[l]
                    # Update ans if this sum is larger
                    ans = max(ans, cur_sum)
        # Return the maximum fruits harvested
        return ans

    maxTotalFruits = max_total_fruits
