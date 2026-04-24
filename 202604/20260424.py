# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    """2833. Furthest Point From Origin
    
    You are given a string moves of length n consisting only of characters 'L',
    'R', and '_'. The string represents your movement on a number line starting
    from the origin 0.
    
    In the ith move, you can choose one of the following directions:
    move to the left if moves[i] = 'L' or moves[i] = '_'
    move to the right if moves[i] = 'R' or moves[i] = '_'
    
    Return the distance from the origin of the furthest point you can get to
    after n moves.
    """
    def furthest_distance_from_origin(self, moves: str) -> int:
        # Count net movement and wildcards in one pass
        net = 0
        underscores = 0
        for move in moves:
            if move == "R":
                net += 1
            elif move == "L":
                net -= 1
            else:
                underscores += 1
        # Furthest is always |net| + underscores by assigning all
        # _ in the direction that increases magnitude
        return abs(net) + underscores

    furthestDistanceFromOrigin = furthest_distance_from_origin