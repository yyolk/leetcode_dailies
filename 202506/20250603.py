# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/


class Solution:
    """1298. Maximum Candies You Can Get from Boxes

    You have `n` boxes labeled from `0` to `n - 1`. You are given four arrays: `status`,
    `candies`, `keys`, and `contained_boxes` where:

    * `status[i]` is `1` if the `ith` box is open and `0` if the `ith` box is closed,

    * `candies[i]` is the number of candies in the `ith` box,

    * `keys[i]` is a list of the labels of the boxes you can open after opening the
    `ith` box.

    * `contained_boxes[i]` is a list of the boxes you found inside the `ith` box.

    You are given an integer array `initial_boxes` that contains the labels of the boxes
    you initially have. You can take all the candies in **any open box** and you can use
    the keys in it to open new boxes and you also can use the boxes you find in it.

    Return *the maximum number of candies you can get following the rules above*."""

    def max_candies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        contained_boxes: list[list[int]],
        initial_boxes: list[int],
    ) -> int:
        # Initialize sets to track state
        accessible = set(initial_boxes)  # Boxes we have access to
        have_key = set()                 # Boxes we have keys for
        opened = set()                   # Boxes we have opened
        total_candies = 0                # Total candies collected
        
        # Initially, we can open any accessible box that has status 1
        openable = set(box for box in accessible if status[box] == 1)
        
        # Process boxes as long as there are boxes we can open
        while openable:
            box = openable.pop()  # Take a box we can open
            if box in opened:
                continue  # Skip if already opened (safety check)
            
            # Open the box and collect its candies
            opened.add(box)
            total_candies += candies[box]
            
            # Add all keys found in this box to our key set
            for key in keys[box]:
                have_key.add(key)
                # If this key unlocks an accessible, unopened, initially closed box,
                # we can now open it
                if key in accessible and key not in opened and status[key] == 0:
                    openable.add(key)
            
            # Add all contained boxes to accessible set
            for contained in contained_boxes[box]:
                if contained not in accessible:
                    accessible.add(contained)
                    # If this contained box can be opened (either initially open or we have its key),
                    # add it to openable
                    if contained not in opened and (status[contained] == 1 or contained in have_key):
                        openable.add(contained)
        
        return total_candies

    maxCandies = max_candies
