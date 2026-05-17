# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/


class Solution:
    """2948. Make Lexicographically Smallest Array by Swapping Elements

    You are given a **0-indexed** array of **positive** integers `nums` and a
    **positive** integer `limit`.

    In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and
    `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

    Return *the **lexicographically smallest array** that can be obtained by performing
    the operation any number of times*.

    An array `a` is lexicographically smaller than an array `b` if in the first position
    where `a` and `b` differ, array `a` has an element that is less than the
    corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically
    smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`."""

    def lexicographically_smallest_array(
        self, nums: list[int], limit: int
    ) -> list[int]:
        # Get the length of the input array
        n = len(nums)

        # Create sorted list of (value, original index) pairs sorted by value
        sorted_pairs = sorted((nums[i], i) for i in range(n))

        # Initialize result array with zeros
        result = [0] * n

        # Track current group of swappable elements and previous value
        current_group = []
        prev_val = None

        # Process each element in sorted order
        for val, idx in sorted_pairs:
            if not current_group:
                # Start first group
                current_group.append((val, idx))
                prev_val = val
            else:
                if val - prev_val <= limit:
                    # Add to current group if within limit
                    current_group.append((val, idx))
                    prev_val = val
                else:
                    # Finalize current group when limit exceeded
                    # Sort original indices within group
                    sorted_indices = sorted(i for (v, i) in current_group)
                    # Get sorted values for the group
                    sorted_values = [v for (v, i) in current_group]
                    # Assign values to sorted positions
                    for pos, idx_sorted in enumerate(sorted_indices):
                        result[idx_sorted] = sorted_values[pos]
                    # Start new group with current element
                    current_group = [(val, idx)]
                    prev_val = val

        # Process remaining elements in the last group
        if current_group:
            sorted_indices = sorted(i for (v, i) in current_group)
            sorted_values = [v for (v, i) in current_group]
            for pos, idx_sorted in enumerate(sorted_indices):
                result[idx_sorted] = sorted_values[pos]

        return result

    lexicographicallySmallestArray = lexicographically_smallest_array
