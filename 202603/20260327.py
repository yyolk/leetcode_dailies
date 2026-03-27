# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts

class Solution:
    """2946. Matrix Similarity After Cyclic Shifts
    
    You are given an m x n integer matrix mat and an integer k. The matrix rows are
    0-indexed. The following process happens k times: Even-indexed rows (0, 2, 4, ...)
    are cyclically shifted to the left. Odd-indexed rows (1, 3, 5, ...) are cyclically
    shifted to the right. Return true if the final modified matrix after k steps is
    identical to the original matrix, and false otherwise.
    """
    def are_similar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        # effective shift amount (cyclic property repeats every n steps)
        shift = k % n
        for i in range(len(mat)):
            row = mat[i]
            if i % 2 == 0:
                # even row: left cyclic shift by shift positions
                if row[shift:] + row[:shift] != row:
                    return False
            else:
                # odd row: right cyclic shift by shift positions
                if row[-shift:] + row[:-shift] != row:
                    return False
        return True

    areSimilar = are_similar