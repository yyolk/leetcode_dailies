# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
from collections import deque, defaultdict


class Solution:
    """2115. Find All Possible Recipes from Given Supplies

    You have information about `n` different recipes. You are given a string array
    `recipes` and a 2D string array `ingredients`. The `ith` recipe has the name
    `recipes[i]`, and you can **create** it if you have **all** the needed ingredients
    from `ingredients[i]`. A recipe can also be an ingredient for **other** recipes,
    i.e., `ingredients[i]` may contain a string that is in `recipes`.

    You are also given a string array `supplies` containing all the ingredients that you
    initially have, and you have an infinite supply of all of them.

    Return *a list of all the recipes that you can create.* You may return the answer in
    **any order**.

    Note that two recipes may contain each other in their ingredients."""

    def find_all_recipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        # Convert supplies to a set for O(1) lookup
        supplies_set = set(supplies)

        # Build a graph where each ingredient points to recipes that need it
        graph = defaultdict(list)

        # Calculate initial indegree for each recipe (dependencies not in supplies)
        indegree = {}

        # Populate graph and indegree
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
            indegree[recipe] = sum(
                1 for ingredient in ingredients[i] if ingredient not in supplies_set
            )

        # Initialize queue with recipes that have no dependencies (indegree 0)
        queue = deque([recipe for recipe in recipes if indegree.get(recipe, 0) == 0])

        # List to store recipes that can be made
        made_recipes = []

        # Process recipes using BFS
        while queue:
            recipe = queue.popleft()
            made_recipes.append(recipe)
            # For each recipe that depends on the current recipe
            for neighbor in graph[recipe]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return made_recipes

    findAllRecipes = find_all_recipes
