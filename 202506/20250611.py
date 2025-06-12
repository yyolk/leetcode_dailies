# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/


class Solution:
    """3445. Maximum Difference Between Even and Odd Frequency II

    You are given a string `s` and an integer `k`. Your task is to find the **maximum**
    difference between the frequency of **two** characters, `freq[a] - freq[b]`, in a
    substring `subs` of `s`, such that:

    * `subs` has a size of **at least** `k`.

    * Character `a` has an *odd frequency* in `subs`.

    * Character `b` has an *even frequency* in `subs`.

    Return the **maximum** difference.

    **Note** that `subs` can contain more than 2 **distinct** characters."""

    def max_difference(self, s: str, min_length: int) -> int:
        # Get the length of the input string
        string_length = len(s)
        # Initialize the maximum difference to negative infinity
        max_diff_result = float("-inf")

        # Iterate over all possible characters for "a" (first character)
        for char_a in "01234":
            # Iterate over all possible characters for "b" (second character)
            for char_b in "01234":
                # Skip if both characters are the same
                if char_a == char_b:
                    continue

                # Create an array where char_a is 1, char_b is -1, and others are 0
                difference_array = [
                    1 if char == char_a else (-1 if char == char_b else 0) for char in s
                ]
                # Create an array to track occurrences of char_a (1 if char_a, else 0)
                char_a_count_array = [1 if char == char_a else 0 for char in s]
                # Create an array to track occurrences of char_b (1 if char_b, else 0)
                char_b_count_array = [1 if char == char_b else 0 for char in s]

                # Initialize prefix sum arrays with an extra element for index 0
                prefix_sum_diff = [0] * (
                    string_length + 1
                )  # For freq[char_a] - freq[char_b]
                prefix_sum_char_a = [0] * (string_length + 1)  # For freq[char_a]
                prefix_sum_char_b = [0] * (string_length + 1)  # For freq[char_b]

                # Compute the prefix sums for all arrays
                for i in range(string_length):
                    prefix_sum_diff[i + 1] = prefix_sum_diff[i] + difference_array[i]
                    prefix_sum_char_a[i + 1] = (
                        prefix_sum_char_a[i] + char_a_count_array[i]
                    )
                    prefix_sum_char_b[i + 1] = (
                        prefix_sum_char_b[i] + char_b_count_array[i]
                    )

                # 2x2 array to store minimum prefix sums for each parity combination
                # Rows: parity of char_a (0: even, 1: odd), Columns: parity of char_b (0: even, 1: odd)
                min_prefix_sums = [
                    [float("inf"), float("inf")],
                    [float("inf"), float("inf")],
                ]

                # Left pointer for the sliding window
                left_pointer = 0

                # Iterate over all possible right endpoints of the substring
                for right_pointer in range(string_length + 1):
                    # Adjust the left pointer to satisfy minimum length and presence conditions
                    while (
                        right_pointer - left_pointer >= min_length
                        and prefix_sum_char_a[right_pointer]
                        - prefix_sum_char_a[left_pointer]
                        > 0
                        and prefix_sum_char_b[right_pointer]
                        - prefix_sum_char_b[left_pointer]
                        > 0
                    ):
                        # Update the minimum prefix sum for the current parity combination at left_pointer
                        min_prefix_sums[prefix_sum_char_a[left_pointer] % 2][
                            prefix_sum_char_b[left_pointer] % 2
                        ] = min(
                            min_prefix_sums[prefix_sum_char_a[left_pointer] % 2][
                                prefix_sum_char_b[left_pointer] % 2
                            ],
                            prefix_sum_diff[left_pointer],
                        )
                        # Move the left pointer to shrink the window
                        left_pointer += 1

                    # Target parity for char_a to be odd: 1 - (current parity of char_a)
                    target_char_a_parity = 1 - (prefix_sum_char_a[right_pointer] % 2)
                    # Target parity for char_b to be even: current parity of char_b
                    target_char_b_parity = prefix_sum_char_b[right_pointer] % 2

                    # Update the maximum difference if a valid minimum prefix sum exists
                    if min_prefix_sums[target_char_a_parity][
                        target_char_b_parity
                    ] != float("inf"):
                        current_diff = (
                            prefix_sum_diff[right_pointer]
                            - min_prefix_sums[target_char_a_parity][
                                target_char_b_parity
                            ]
                        )
                        max_diff_result = max(max_diff_result, current_diff)

        # Return the maximum difference found
        return max_diff_result

    maxDifference = max_difference
