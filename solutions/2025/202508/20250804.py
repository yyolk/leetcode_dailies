# https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    """904. Fruit Into Baskets

    You are visiting a farm that has a single row of fruit trees arranged from left to
    right. The trees are represented by an integer array `fruits` where `fruits[i]` is
    the **type** of fruit the `ith` tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict
    rules that you must follow:

    * You only have **two** baskets, and each basket can only hold a **single type** of
    fruit. There is no limit on the amount of fruit each basket can hold.

    * Starting from any tree of your choice, you must pick **exactly one fruit** from
    **every** tree (including the start tree) while moving to the right. The picked
    fruits must fit in one of your baskets.

    * Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

    Given the integer array `fruits`, return *the **maximum** number of fruits you can
    pick*."""

    def total_fruit(self, fruits: list[int]) -> int:
        # Check if the fruits list is empty; if so, return 0 since no fruits can be picked
        if not fruits:
            return 0
        # Import defaultdict from collections to use a dictionary that provides default values
        from collections import defaultdict

        # Initialize a counter using defaultdict to keep track of fruit types in the current window
        counter = defaultdict(int)
        # Initialize the left pointer for the sliding window
        left = 0
        # Initialize the variable to keep track of the maximum length of valid subarray
        max_len = 0
        # Iterate over the fruits list with the right pointer
        for right in range(len(fruits)):
            # Increment the count of the current fruit type in the counter
            counter[fruits[right]] += 1
            # While there are more than 2 types of fruits in the counter, shrink the window from the left
            while len(counter) > 2:
                # Decrement the count of the fruit type at the left pointer
                counter[fruits[left]] -= 1
                # If the count of the fruit type becomes zero, remove it from the counter
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                # Move the left pointer to the right
                left += 1
            # Update the maximum length with the current window size
            max_len = max(max_len, right - left + 1)
        # Return the maximum length found
        return max_len

    totalFruit = total_fruit
