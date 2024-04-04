# https://leetcode.com/problems/word-search/
from collections import Counter


class Solution:
    """79. Word Search

    Given an `m x n` grid of characters `board` and a string `word`, return `true` *if*
    `word` *exists in the grid*.

    The word can be constructed from letters of sequentially adjacent cells, where
    adjacent cells are horizontally or vertically neighboring. The same letter cell may
    not be used more than once.

    """

    def find_words(self, board, words):
        res = []
        for word in words:
            if self.exist(board, word) == True:
                res.append(word)
        return res

    def exist(self, board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        # if the length of word is greater than the total number of characters in board
        if len(word) > R * C:
            return False

        # Count the occurrences of characters in the board
        count = Counter(sum(board, []))

        # Check if the count of a letter in the word is greater than its count in the board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        # If the count of the first letter of word is greater than that of the last one in board
        # Reverse search the word for optimization
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        # Use backtracking to search for the word in the board
        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or word[i] != board[r][c]
                or (r, c) in seen
            ):
                return False

            seen.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Backtracking: remove the visited cell
            seen.remove((r, c))
            return res

        # Start DFS from each cell in the board
        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True

        return False
