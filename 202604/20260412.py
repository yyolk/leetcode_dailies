# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers

class Solution:
    """1320. Minimum Distance to Type a Word Using Two Fingers
    
    You have a keyboard layout as shown above in the X-Y plane, where each
    English uppercase letter is located at some coordinate. For example, the
    letter "A" is located at coordinate (0, 0), the letter "B" is located at
    coordinate (0, 1), the letter "P" is located at coordinate (2, 3) and the
    letter "Z" is located at coordinate (4, 1). Given the string word, return
    the minimum total distance to type such string using only two fingers. The
    distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 -
    y2|. Note that the initial positions of your two fingers are considered
    free so do not count towards your total distance, also your two fingers do
    not have to start at the first letter or the first two letters.
    """
    def minimum_distance(self, word: str) -> int:
        # precompute (row, col) for letters A-Z (0-25)
        pos = [(i // 6, i % 6) for i in range(26)]
        n = len(word)
        INF = 10**9
        # prev[a][b]: min cost after typing i letters (finger1 at a, 26=none)
        prev = [[INF] * 27 for _ in range(27)]
        prev[26][26] = 0
        for i in range(n):
            let = ord(word[i]) - ord("A")
            curr = [[INF] * 27 for _ in range(27)]
            for a in range(27):
                for b in range(27):
                    if prev[a][b] == INF:
                        continue
                    # move finger1 to current letter (0 cost if unused)
                    cost = (0 if a == 26 else
                            abs(pos[a][0] - pos[let][0]) + abs(pos[a][1] - pos[let][1]))
                    curr[let][b] = min(curr[let][b], prev[a][b] + cost)
                    # move finger2 to current letter (0 cost if unused)
                    cost = (0 if b == 26 else
                            abs(pos[b][0] - pos[let][0]) + abs(pos[b][1] - pos[let][1]))
                    curr[a][let] = min(curr[a][let], prev[a][b] + cost)
            prev = curr
        # minimum cost over all final finger positions
        return min(min(row) for row in prev)

    minimumDistance = minimum_distance