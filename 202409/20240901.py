# https://leetcode.com/problems/convert-1d-array-into-2d-array/


class Solution:
    """2022. Convert 1D Array Into 2D Array

    You are given a **0\\-indexed** 1\\-dimensional (1D) integer array `original`, and two
    integers, `m` and `n`. You are tasked with creating a 2\\-dimensional (2D) array with
    `m` rows and `n` columns using **all** the elements from `original`.

    The elements from indices `0` to `n - 1` (**inclusive**) of `original` should form
    the first row of the constructed 2D array, the elements from indices `n` to `2 * n -
    1` (**inclusive**) should form the second row of the constructed 2D array, and so
    on.

    Return *an* `m x n` *2D array constructed according to the above procedure, or an
    empty 2D array if it is impossible*.

    """

    def construct2_d_array(
        self, original: list[int], m: int, n: int
    ) -> list[list[int]]:
        # Check if the total number of elements in original can fill an m x n array
        if len(original) != m * n:
            # Return empty list if it's impossible to construct the 2D array
            return []

        # Initialize the result 2D list
        result = []

        # Iterate over the range of m to create each row
        for i in range(m):
            # Slice the original list to get elements for the current row
            # i*n is the start index, (i+1)*n is the end index for each row
            result.append(original[i*n : (i+1)*n])

        return result

    construct2DArray = construct2_d_array
