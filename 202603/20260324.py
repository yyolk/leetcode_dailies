# https://leetcode.com/problems/construct-product-matrix


class Solution:
    """2906. Construct Product Matrix
    
    Given a 0-indexed 2D integer matrix grid of size n * m, we define a 
    0-indexed 2D matrix p of size n * m as the product matrix of grid if the 
    following condition is met: Each element p[i][j] is calculated as the 
    product of all elements in grid except for the element grid[i][j]. This 
    product is then taken modulo 12345. Return the product matrix of grid.
    """
    def construct_product_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0]) if n else 0
        mod = 12345
        p = [[0] * m for _ in range(n)]
        # suffix product starts at 1 (product of elements after current)
        suf = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # store suffix (all after) in output matrix
                p[i][j] = suf
                # update suffix to include current element
                suf = (suf * grid[i][j]) % mod
        # prefix product starts at 1 (product of elements before current)
        pre = 1
        for i in range(n):
            for j in range(m):
                # multiply stored suffix by prefix
                p[i][j] = (p[i][j] * pre) % mod
                # update prefix to include current element
                pre = (pre * grid[i][j]) % mod
        return p

    constructProductMatrix = construct_product_matrix