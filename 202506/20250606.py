# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/


class Solution:
    """2434. Using a Robot to Print the Lexicographically Smallest String

    You are given a string `s` and a robot that currently holds an empty string `t`.
    Apply one of the following operations until `s` and `t` **are both empty**:

    * Remove the **first** character of a string `s` and give it to the robot. The robot
    will append this character to the string `t`.

    * Remove the **last** character of a string `t` and give it to the robot. The robot
    will write this character on paper.

    Return *the lexicographically smallest string that can be written on the paper.*"""

    def robot_with_string(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        # Precompute the smallest character in the suffix s[i:]
        min_suffix = [0] * n
        min_suffix[-1] = s[-1]
        for i in range(n-2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i+1])
        
        # Initialize stack t, result list paper, and index i
        t = []
        paper = []
        i = 0
        
        # Process until both s and t are empty
        while i < n or t:
            if t and (i == n or t[-1] <= min_suffix[i]):
                paper.append(t.pop())
            else:
                t.append(s[i])
                i += 1
        
        return "".join(paper)

    robotWithString = robot_with_string
