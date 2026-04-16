# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array

class Solution:
    """2515. Shortest Distance to Target String in a Circular Array
    
    You are given a 0-indexed circular string array words and a string target. A
    circular array means that the array's end connects to the array's beginning.
    Formally, the next element of words[i] is words[(i + 1) % n] and the previous
    element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
    Starting from startIndex, you can move to either the next word or the previous
    word with 1 step at a time.
    Return the shortest distance needed to reach the string target. If the string
    target does not exist in words, return -1.
    """
    def closest_target(self, words: list[str], target: str, start_index: int) -> int:
        # length of the circular array
        n = len(words)
        # initialize to -1 (target not found)
        ans = -1
        for i in range(n):
            if words[i] == target:
                # compute minimum steps (clockwise vs counterclockwise)
                dist = min(abs(i - start_index), n - abs(i - start_index))
                if ans == -1 or dist < ans:
                    ans = dist
        return ans

    closestTarget = closest_target