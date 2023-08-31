class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """1326. Minimum Number of Taps to Open to Water a Garden

        There is a one-dimensional garden on the x-axis. 
        The garden starts at the point `0` and ends at the point `n`. 
        (i.e The length of the garden is `n`).

        There are `n + 1` taps located at points `[0, 1, ..., n]` in the garden.

        Given an integer `n` and an integer array ranges of length `n + 1` 
        where `ranges[i]` (0-indexed) means the `i-th` tap can water the 
        area `[i - ranges[i], i + ranges[i]]` if it was open.

        Return the minimum number of taps that should be open to water the whole garden, 
        If the garden cannot be watered return -1.

        Args:
            n (int): How many taps there are in the garden
            ranges (List of int): A range to cover in the garden
        
        Returns:
            int: _The minimum number of taps that should be open to water the whole garden._
                If the garden cannot be watered return **-1**
        """
        # Initialize an array with 0 for the starting point and n+2 for all others
        dp = [0] + [n + 2] * n

        # Iterate through each tap and its range
        for idx, i in enumerate(ranges):
            # Calculate the interval that this tap can cover
            left = max(idx - i + 1, 0)
            right = min(idx + i, n)

            # Update the array to store the minimum number of taps needed to cover  the interval
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[max(0, idx - i)] + 1)

        # If the last element of the array is still n+2, it means the garden cannot be watered (-1)
        # Otherwise, return the minimum number of taps needed for the entire garden
        return dp[n] if dp[n] < n + 2 else -1