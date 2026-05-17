# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/


class Solution:
    """3160. Find the Number of Distinct Colors Among the Balls

    You are given an integer `limit` and a 2D array `queries` of size `n x 2`.

    There are `limit + 1` balls with **distinct** labels in the range `[0, limit]`.
    Initially, all balls are uncolored. For every query in `queries` that is of the form
    `[x, y]`, you mark ball `x` with the color `y`. After each query, you need to find
    the number of **distinct** colors among the balls.

    Return an array `result` of length `n`, where `result[i]` denotes the number of
    distinct colors *after* `ith` query.

    **Note** that when answering a query, lack of a color *will not* be considered as a
    color."""

    def query_results(self, limit: int, queries: list[list[int]]) -> list[int]:
        # Ball -> Color
        colors = {}
        distinct_colors = set()
        # Color -> Count
        color_counts = {}
        result = []

        for x, y in queries:
            old_color = colors.get(x)

            # New ball
            if old_color is None:
                if y not in distinct_colors:
                    distinct_colors.add(y)
                # Increment count
                color_counts[y] = color_counts.get(y, 0) + 1
            # Color change
            elif old_color != y:
                # Decrement old color count
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    distinct_colors.remove(old_color)

                if y not in distinct_colors:
                    distinct_colors.add(y)
                # Increment new color count
                color_counts[y] = color_counts.get(y, 0) + 1

            colors[x] = y
            result.append(len(distinct_colors))

        return result

    queryResults = query_results
