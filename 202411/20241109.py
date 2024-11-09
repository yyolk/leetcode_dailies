# https://leetcode.com/problems/minimum-array-end/


class Solution:
    """3133. Minimum Array End

    You are given two integers `n` and `x`. You have to construct an array of
    **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i +
    1]` is **greater than** `nums[i]`, and the result of the bitwise `AND` operation
    between all elements of `nums` is `x`.

    Return the **minimum** possible value of `nums[n - 1]`.

    """

    def min_end(self, n: int, x: int) -> int:
        # Initialize position for bit manipulation
        pos = 0
        # Decrement n by 1 because we start with x, so we only need n-1 more numbers to increase
        n -= 1
        
        # Loop to construct the next n-1 numbers
        while n > 0:
            # Get the least significant bit of n
            bit = n & 1
            # Right shift n to continue with the next bit
            n = n >> 1
            
            # Find the next available bit position where x has a zero
            while x & (1 << pos) > 0:
                pos += 1
            
            # XOR the bit into x at the found position, effectively setting or unsetting the bit
            x = x ^ (bit << pos)
            # Move to the next bit position
            pos += 1
        
        # At this point, x represents the last number in our sequence
        return x

    minEnd = min_end
