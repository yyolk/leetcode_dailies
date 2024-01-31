# https://leetcode.com/problems/daily-temperatures/


class Solution:
    """739. Daily Temperatures

    Given an array of integers `temperatures` represents the daily temperatures, return
    *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait
    after the* `ith` *day to get a warmer temperature*. If there is no future day for
    which this is possible, keep `answer[i] == 0` instead.

    """

    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        # Initialize the answer array with zeros
        answer = [0] * n
        # Stack to keep track of indices
        stack = []

        for i in range(n):
            # Check if the current temperature is greater than the temperature at the index at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Update the answer for the index at the top of the stack
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            # Push the current index onto the stack
            stack.append(i)

        return answer

    dailyTemperatures = daily_temperatures
