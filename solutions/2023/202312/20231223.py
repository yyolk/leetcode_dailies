# https://leetcode.com/problems/path-crossing/


class Solution:
    """1496. Path Crossing

    Given a string `path`, where `path[i] = 'N'`, `'S'`, `'E'` or `'W'`, each
    representing moving one unit north, south, east, or west, respectively. You start at
    the origin `(0, 0)` on a 2D plane and walk on the path specified by `path`.

    Return `true` *if the path crosses itself at any point, that is, if at any time you
    are on a location you have previously visited*. Return `false` otherwise.
    """

    def is_path_crossing(self, path: str) -> bool:
        # Initialize tracking coords.
        x, y = 0, 0
        # Initialize visited coords set().
        visited = set()
        # Add origin (starting point) to visited.
        visited.add((x, y))

        # Each character in path is a cardinal direction.
        for move in path:
            match move:
                case "N":
                    y += 1
                case "S":
                    y -= 1
                case "E":
                    x += 1
                case "W":
                    x -= 1
            # Check if the current position is already visited.
            if (x, y) in visited:
                return True

            # Add the current position, (x, y) coords, to visited.
            visited.add((x, y))

        # We never crossed our path.
        return False

    isPathCrossing = is_path_crossing
