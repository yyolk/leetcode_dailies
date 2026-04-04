# https://leetcode.com/problems/decode-the-slanted-ciphertext

class Solution:
    """2075. Decode the Slanted Ciphertext
    
    A string originalText is encoded using a slanted transposition cipher to a
    string encodedText with the help of a matrix having a fixed number of rows
    rows. originalText is placed first in a top-left to bottom-right manner.
    All empty cells are filled with ' '. The number of columns is chosen such
    that the rightmost column will not be empty after filling in originalText.
    encodedText is then formed by appending all characters of the matrix in a
    row-wise fashion. Given the encoded string encodedText and number of rows
    rows, return the original string originalText. Note: originalText does not
    have any trailing spaces ' '. The test cases are generated such that there
    is only one possible originalText.
    """
    def decode_ciphertext(self, encoded_text: str, rows: int) -> str:
        # Calculate number of columns from encoded length
        cols = len(encoded_text) // rows
        ans = []
        # Traverse each possible starting column on top row
        for j in range(cols):
            # Start at row 0, current column j
            x, y = 0, j
            # Follow the down-right diagonal
            while x < rows and y < cols:
                # Access matrix position via flat index
                ans.append(encoded_text[x * cols + y])
                x += 1
                y += 1
        # Join and remove trailing spaces
        return "".join(ans).rstrip()

    decodeCiphertext = decode_ciphertext