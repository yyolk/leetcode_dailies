# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k
from collections import deque


class Solution:
    """3578. Count Partitions With Max-Min Difference at Most K

    Given an integer array nums and an integer k, partition nums into one or
    more non-empty contiguous segments where in each segment max - min <= k.
    Return the number of ways to do this, modulo 10^9 + 7.
    """
    def count_partitions(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        # ways_dynamic_programming[i] = number of ways to partition nums[0..i-1]
        ways_dynamic_programming = [1]  # Base case: 1 way for empty prefix
        # total_ways_count maintains sum of ways_dynamic_programming[j] for valid j up to current
        total_ways_count = 1
        # left_pointer: leftmost index for valid segment ending at right_index
        left_pointer = 0
        # min_value_index_queue: indices in increasing order of nums values (for min)
        min_value_index_queue = deque()
        # max_value_index_queue: indices in decreasing order of nums values (for max)
        max_value_index_queue = deque()
        
        for right_index, current_number in enumerate(nums):
            # Maintain max_value_index_queue (decreasing): remove smaller from end
            while max_value_index_queue and current_number > nums[max_value_index_queue[-1]]:
                max_value_index_queue.pop()
            max_value_index_queue.append(right_index)
            # Maintain min_value_index_queue (increasing): remove larger from end
            while min_value_index_queue and current_number < nums[min_value_index_queue[-1]]:
                min_value_index_queue.pop()
            min_value_index_queue.append(right_index)
            # Shrink from left until max - min <= k in window [left_pointer, right_index]
            while max_value_index_queue and min_value_index_queue and \
                  nums[max_value_index_queue[0]] - nums[min_value_index_queue[0]] > k:
                # Subtract ways starting at old left_pointer (cannot extend to right_index)
                total_ways_count = (total_ways_count - ways_dynamic_programming[left_pointer] + MOD) % MOD
                left_pointer += 1
                # Remove indices < left_pointer from queues
                if min_value_index_queue and left_pointer > min_value_index_queue[0]:
                    min_value_index_queue.popleft()
                if max_value_index_queue and left_pointer > max_value_index_queue[0]:
                    max_value_index_queue.popleft()
            # ways_dynamic_programming[right_index + 1] = sum of valid previous ways (extendable)
            ways_dynamic_programming.append(total_ways_count)
            # Update total_ways_count = 2 * current (old sum + new ways for starting new segment)
            total_ways_count = (total_ways_count * 2) % MOD
        
        return ways_dynamic_programming[-1]
       
    countPartitions = count_partitions