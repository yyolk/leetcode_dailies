# https://leetcode.com/problems/filling-bookcase-shelves/


class Solution:
    """1105. Filling Bookcase Shelves

    You are given an array `books` where `books[i] = [thicknessi, heighti]` indicates
    the thickness and height of the `ith` book. You are also given an integer
    `shelf_width`.

    We want to place these books in order onto bookcase shelves that have a total width
    `shelf_width`.

    We choose some of the books to place on this shelf such that the sum of their
    thickness is less than or equal to `shelf_width`, then build another level of the
    shelf of the bookcase so that the total height of the bookcase has increased by the
    maximum height of the books we just put down. We repeat this process until there are
    no more books to place.

    Note that at each step of the above process, the order of the books we place is the
    same order as the given sequence of books.

    * For example, if we have an ordered list of `5` books, we might place the first and
    second book onto the first shelf, the third book on the second shelf, and the fourth
    and fifth book on the last shelf.

    Return *the minimum possible height that the total bookshelf can be after placing
    shelves in this manner*.

    """

    def min_height_shelves(self, books: list[list[int]], shelf_width: int) -> int:
        n = len(books)
        # dp[i] will store the minimum height of the bookshelf for the first i books
        dp = [float("inf")] * (n + 1)
        # No books means no height
        dp[0] = 0
        
        # Iterate over each book
        for i in range(1, n + 1):
            # Initialize current shelf width and height
            width = 0
            height = 0
            # Try to place books from j to i on the current shelf
            for j in range(i, 0, -1):
                # Accumulate the width of the books
                width += books[j - 1][0]
                # If the accumulated width exceeds the shelf width, break
                if width > shelf_width:
                    break
                # Update the maximum height of the current shelf
                height = max(height, books[j - 1][1])
                # Update dp[i] with the minimum possible height
                dp[i] = min(dp[i], dp[j - 1] + height)
        
        # Return the minimum height of the bookshelf for all books
        return dp[n]

    minHeightShelves = min_height_shelves
