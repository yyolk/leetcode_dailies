# https://leetcode.com/problems/design-a-food-rating-system/
from sortedcontainers import SortedSet


class FoodRatings:
    """2353. Design a Food Rating System."""

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with cuisine it belongs to.
        self.food_cuisine_map = {}

        # Store all food of a cuisine in a set (to sort them on ratings/name)
        # Set element -> Tuple: (-1 * food_rating, food_name)
        self.cuisine_food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map'
            # and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(-1 * rating, name)' element in the current cuisine's set.
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def change_rating(self, food: str, new_rating: int) -> None:
        # Fetch cuisine name for food.
        cuisine_name = self.food_cuisine_map[food]

        # Find and delete the element from the respective cuisine's set.
        old_element = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_element)

        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = new_rating
        # Insert the '(-1 * new rating, name)' element in the respective cuisine's set.
        self.cuisine_food_map[cuisine_name].add((-new_rating, food))

    def highest_rated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        # Return name of the highest-rated 'food' of 'cuisine'.
        return highest_rated[1]

    changeRating = change_rating
    highestRated = highest_rated


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
