# https://leetcode.com/problems/find-if-array-can-be-sorted/


class Solution:
    """3011. Find if Array Can Be Sorted

    You are given a **0\\-indexed** array of **positive** integers `nums`.

    In one **operation**, you can swap any two **adjacent** elements if they have the
    **same** number of set bits. You are allowed to do this operation **any** number of
    times (**including zero**).

    Return `true` *if you can sort the array, else return* `false`.

    """

    def can_sort_array(self, nums: list[int]) -> bool:
        min_group, max_group, max_prev_group = float("inf"), float("-inf"), float("-inf")
        prev_bit_cnt = None

        for i, num in enumerate(nums):
            bit_cnt = num.bit_count()
            if bit_cnt != prev_bit_cnt:
                # Check if the previous group"s max is less than the current group"s min
                if max_prev_group > min_group and max_prev_group != float("-inf"):
                    return False

                # Update max_prev_group for the next check
                max_prev_group = max_group if max_group != float("-inf") else float("-inf")
                min_group, max_group = num, num
            else:
                # Update min and max for the current group
                min_group = min(min_group, num)
                max_group = max(max_group, num)
            prev_bit_cnt = bit_cnt

        # Final check to ensure the last group does not overlap with any previous max
        return max_prev_group < min_group

    canSortArray = can_sort_array
