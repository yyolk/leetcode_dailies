# https://leetcode.com/problems/maximum-swap/


class Solution:
    """670. Maximum Swap

    You are given an integer `num`. You can swap two digits at most once to get the
    maximum valued number.

    Return *the maximum valued number you can get*.

    """

    def maximum_swap(self, num: int) -> int:
        # Convert number to list of digits for easy manipulation
        num_list = list(str(num))
        last_occurrence = {int(d): i for i, d in enumerate(num_list)}

        # Iterate through the digits from left to right
        for i, d in enumerate(num_list):
            # We want to swap with the largest digit that is greater than the current digit
            # and appears later in the number
            for j in range(9, int(d), -1):
                if last_occurrence.get(j, -1) > i:
                    # Perform the swap
                    num_list[i], num_list[last_occurrence[j]] = num_list[last_occurrence[j]], num_list[i]
                    # Convert back to integer and return since we can only swap once
                    return int("".join(num_list))
    
        # If no swap occurred, return the original number
        return num

    maximumSwap = maximum_swap
