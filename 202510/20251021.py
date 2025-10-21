# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
from collections import Counter, defaultdict
import bisect


class Solution:
    """3346. Maximum Frequency of an Element After Performing Operations I

    You are given an integer array `nums` and two integers `k` and `num_operations`.

    You must perform an **operation** `num_operations` times on `nums`, where in each
    operation you:

    * Select an index `i` that was **not** selected in any previous operations.

    * Add an integer in the range `[-k, k]` to `nums[i]`.

    Return the **maximum** possible frequency of any element in `nums` after performing
    the **operations**."""

    def max_frequency(self, nums: list[int], k: int, num_operations: int) -> int:

        # Handle empty array case
        if not nums:
            return 0

        # Count the frequency of each element in nums
        freq = Counter(nums)

        # Prepare the difference array for sweep line
        diff = defaultdict(int)

        # For each number, mark the range [num - k, num + k]
        for num in nums:
            diff[num - k] += 1
            diff[num + k + 1] -= 1
            # Ensure original num positions are included in positions
            diff[num] += 0

        # Get sorted list of all positions where differences change
        positions = sorted(diff.keys())

        # Get sorted list of values that appear in nums (forbidden for freq=0)
        forbidden = sorted(freq.keys())

        # Initialize variables for answer and running sum
        ans = 0
        current_sum = 0

        # Sweep through the sorted positions
        for i, pos in enumerate(positions):
            # Update the running count of reachable elements
            current_sum += diff[pos]

            # Calculate for the current position
            already = freq[pos]
            ans = max(ans, min(current_sum, already + num_operations))

            # Check the segment between current and next position
            if i < len(positions) - 1:
                next_pos = positions[i + 1]
                seg_start = pos + 1
                seg_end = next_pos - 1
                if seg_start <= seg_end:
                    # Find number of forbidden values in the segment
                    l = bisect.bisect_left(forbidden, seg_start)
                    r = bisect.bisect_right(forbidden, seg_end)
                    num_forbidden = r - l
                    # Calculate total integers in the segment
                    num_ints = seg_end - seg_start + 1
                    # If there is at least one t with freq=0 in segment
                    if num_forbidden < num_ints:
                        # Update ans for freq=0 case
                        ans = max(ans, min(current_sum, num_operations))

        # Return the maximum frequency found
        return ans

    maxFrequency = max_frequency
