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

    def robot_with_string(self, s: str) -> str: ...

    robotWithString = robot_with_string
