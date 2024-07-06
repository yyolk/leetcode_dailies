# https://leetcode.com/problems/pass-the-pillow/


class Solution:
    """2582. Pass the Pillow

    There are `n` people standing in a line labeled from `1` to `n`. The first person in
    the line is holding a pillow initially. Every second, the person holding the pillow
    passes it to the next person standing in the line. Once the pillow reaches the end
    of the line, the direction changes, and people continue passing the pillow in the
    opposite direction.

    * For example, once the pillow reaches the `nth` person they pass it to the `n -
    1th` person, then to the `n - 2th` person and so on.

    Given the two positive integers `n` and `time`, return *the index of the person
    holding the pillow after* `time` *seconds*.

    """

    def pass_the_pillow(self, n: int, time: int) -> int:
        # The effective time within the current back-and-forth cycle
        cycle_time = time % (2 * (n - 1))
        
        # Determine the current position based on the cycle time
        if cycle_time < n:
            # Moving forward
            return cycle_time + 1
        else:
            # Moving backward
            return n - (cycle_time - (n - 1))

    passThePillow = pass_the_pillow
