# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


class Solution:
    """2698. Find the Punishment Number of an Integer

    Given a positive integer `n`, return *the **punishment number*** of `n`.

    The **punishment number** of `n` is defined as the sum of the squares of all
    integers `i` such that:

    * `1 <= i <= n`

    * The decimal representation of `i * i` can be partitioned into contiguous
    substrings such that the sum of the integer values of these substrings equals `i`.
    """

    def punishment_number(self, n: int) -> int:
        # Helper function to check if the string representation of a square can be partitioned into substrings that sum to the target
        def can_partition(s: str, target: int) -> bool:
            length = len(s)
            # Initialize a DP array where each element is a set of possible sums up to that position
            # dp[i] stores all possible sums achievable by partitioning the first i characters of the string
            dp = [set() for _ in range(length + 1)]
            # Base case: 0 sum can be achieved with 0 characters
            dp[0].add(0)

            # Iterate through each possible end position in the string
            for i in range(1, length + 1):
                # Check all possible starting positions for the current substring
                for j in range(i):
                    # Skip positions where no valid sums were recorded
                    if not dp[j]:
                        continue
                    # Extract the substring from j to i (exclusive of i)
                    num_str = s[j:i]
                    # Skip substrings with leading zeros (invalid number formats)
                    if len(num_str) > 1 and num_str[0] == "0":
                        continue
                    # Convert the substring to an integer
                    num = int(num_str)
                    # Update possible sums for position i by adding the current number to previous sums
                    for prev_sum in dp[j]:
                        current = prev_sum + num
                        # Only track sums that do not exceed the target
                        if current > target:
                            continue
                        dp[i].add(current)
            # Check if the target sum is achievable with the full string
            return target in dp[length]
        
        # Initialize the result to accumulate the sum of valid squares
        result = 0
        # Iterate through all numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            square = i * i
            # Check if the square meets the partitioning condition
            if can_partition(str(square), i):
                # Add the square to the result if valid
                result += square
        return result

    punishmentNumber = punishment_number
