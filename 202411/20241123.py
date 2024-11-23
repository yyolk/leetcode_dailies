# https://leetcode.com/problems/rotating-the-box/


class Solution:
    """1861. Rotating the Box

    You are given an `m x n` matrix of characters `box` representing a side\\-view of a
    box. Each cell of the box is one of the following:

    * A stone `'#'`

    * A stationary obstacle `'*'`

    * Empty `'.'`

    The box is rotated **90 degrees clockwise**, causing some of the stones to fall due
    to gravity. Each stone falls down until it lands on an obstacle, another stone, or
    the bottom of the box. Gravity **does not** affect the obstacles' positions, and the
    inertia from the box's rotation **does not** affect the stones' horizontal
    positions.

    It is **guaranteed** that each stone in `box` rests on an obstacle, another stone,
    or the bottom of the box.

    Return *an* `n x m` *matrix representing the box after the rotation described
    above*.

    """

    def rotate_the_box(self, box: list[list[str]]) -> list[list[str]]:
        # Traverse each row of the original box
        for row in box:
            # Initialize drop position to the last index of the row
            drop_position = len(row) - 1  
            
            # Iterate from right to left
            for current_position in range(len(row) - 1, -1, -1):
                # If we find an obstacle, adjust the drop position
                if row[current_position] == "*":  
                    drop_position = current_position - 1
                # If we find a stone, move it to the drop position
                elif row[current_position] == "#":  
                    # Swap the stone with the empty space at drop_position
                    row[drop_position], row[current_position] = row[current_position], row[drop_position]
                    # Adjust drop position for the next stone
                    drop_position -= 1

        # Rotate the box 90 degrees clockwise
        rotated_box = list(zip(*box[::-1]))
        # Convert zip object to list for return
        return rotated_box

    rotateTheBox = rotate_the_box
