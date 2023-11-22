# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
import heapq


class Solution:
    """1337. The K Weakest Rows in a Matrix

    You are given an `m x n` binary matrix `mat` of `1`'s (representing soldiers) and `0`'s
    (representing civilians). The soldiers are positioned **in front** of the civilians.
    That is, all the `1`'s will appear to the **left** of all the `0`'s in each row.

    A row `i` is **weaker** than a row `j` if one of the following is true:

    * The number of soldiers in row `i` is less than the number of soldiers in row `j`.

    * Both rows have the same number of soldiers and `i < j`.

    Return *the indices of the* `k` ***weakest** rows in the matrix ordered from weakest to
    strongest*.
    """

    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        """K Weakest rows in matrix

        Proposed solution

        Args:
            mat (list of list of int): matrix representing soldiers (1)
                and civilians (0)

        Returns:
            list of int: the k weakest rows in the matrix, ordered from weakest
                to strongest
        """
        # A min-heap to store the weakest rows
        heap = []

        for i, row in enumerate(mat):
            # Calculate the number of soldiers in the row, conveniently repr'd by 1
            num_soldiers = sum(row)

            # Push the negative count and row index onto the heap
            # The negative count ensures that rows with fewer soldiers are at the top
            # When rows have the same count, the smaller row index will be considered
            # weaker
            heapq.heappush(heap, (-num_soldiers, -i))

            # If the heap size exceeds k, pop the strongest row
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the row indices from the heap and reverse the order for weakest first
        weakest_rows = [-heapq.heappop(heap)[1] for _ in range(k)][::-1]

        # Return our k weakest rows
        return weakest_rows
