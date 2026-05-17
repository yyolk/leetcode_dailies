# https://leetcode.com/problems/design-a-food-rating-system/
from collections import defaultdict
import heapq


class FoodRatings:
    """2429. Design a Food Rating System

    Design a food rating system that can do the following:

    * **Modify** the rating of a food item listed in the system.

    * Return the highest-rated food item for a type of cuisine in the system.

    Implement the `FoodRatings` class:

    * `FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the
    system. The food items are described by `foods`, `cuisines` and `ratings`, all of
    which have a length of `n`.

      + `foods[i]` is the name of the `ith` food,

      + `cuisines[i]` is the type of cuisine of the `ith` food, and

      + `ratings[i]` is the initial rating of the `ith` food.

    * `void changeRating(String food, int newRating)` Changes the rating of the food
    item with the name `food`.

    * `String highestRated(String cuisine)` Returns the name of the food item that has
    the highest rating for the given type of `cuisine`. If there is a tie, return the
    item with the **lexicographically smaller** name.

    Note that a string `x` is lexicographically smaller than string `y` if `x` comes
    before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is
    the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in
    alphabetic order.


    Your FoodRatings object will be instantiated and called as such:
        obj = FoodRatings(foods, cuisines, ratings)
        obj.changeRating(food,newRating)
        param_2 = obj.highestRated(cuisine)
    """

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Initialize dictionaries to store food-to-cuisine and food-to-rating mappings
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        # Initialize dictionary to store max heaps for each cuisine
        self.cuisine_to_heap = defaultdict(list)

        # Populate the dictionaries and heaps with initial data
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            # Map food to its cuisine
            self.food_to_cuisine[food] = cuisine
            # Map food to its rating
            self.food_to_rating[food] = rating
            # Push food and rating to cuisine's max heap (negate rating for max heap)
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # Update the rating for the given food
        self.food_to_rating[food] = newRating
        # Get the cuisine for the food
        cuisine = self.food_to_cuisine[food]
        # Push the new rating and food to the cuisine's max heap (negate rating for max heap)
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the heap for the given cuisine
        heap = self.cuisine_to_heap[cuisine]

        # Pop items from the heap until we find a valid one (matching current rating)
        while heap:
            rating, food = heap[0]
            # If the top food's rating matches the current rating in food_to_rating
            if -rating == self.food_to_rating[food]:
                return food
            # Remove outdated entry (lazy deletion)
            heapq.heappop(heap)

        # Return empty string if no valid food is found (should not happen per problem constraints)
        return ""
