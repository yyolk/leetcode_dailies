# https://leetcode.com/problems/image-smoother/


class Solution:
    """661. Image Smoother

    An **image smoother** is a filter of the size `3 x 3` that can be applied to each
    cell of an image by rounding down the average of the cell and the eight surrounding
    cells (i.e., the average of the nine cells in the blue smoother). If one or more of
    the surrounding cells of a cell is not present, we do not consider it in the average
    (i.e., the average of the four cells in the red smoother).

    ![](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

    Given an `m x n` integer matrix `img` representing the grayscale of an image, return
    *the image after applying the smoother on each cell of it*.
    """

    def image_smoother(self, img: list[list[int]]) -> list[list[int]]:
        # Get the number of rows and columns in the input matrix
        rows, cols = len(img), len(img[0])

        # Initialize an empty matrix with the same dimensions as the input image
        result = [[0] * cols for _ in range(rows)]

        # Iterate through each cell in the input image
        for i in range(rows):
            for j in range(cols):
                sum_val, count = 0, 0

                # Iterate through the 3x3 neighborhood of the current cell
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        # Check if the neighboring cell is within the bounds of the image
                        if 0 <= ni < rows and 0 <= nj < cols:
                            # Accumulate the sum and count for the valid neighboring cells
                            sum_val += img[ni][nj]
                            count += 1

                # Calculate the rounded-down average and update the result matrix
                result[i][j] = sum_val // count

        # Return the smoothed image matrix
        return result

    imageSmoother = image_smoother
