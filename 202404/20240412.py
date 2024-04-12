# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    """42. Trapping Rain Water

    Given `n` non-negative integers representing an elevation map where the width of
    each bar is `1`, compute how much water it can trap after raining.

    """

    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        # Initialize two pointers
        left, right = 0, len(height) - 1
        # Initialize max heights
        left_max, right_max = height[left], height[right]

        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water