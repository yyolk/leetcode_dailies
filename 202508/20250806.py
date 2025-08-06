# https://leetcode.com/problems/fruits-into-baskets-iii/


class Solution:
    """3479. Fruits Into Baskets III

    You are given two arrays of integers, `fruits` and `baskets`, each of length `n`,
    where `fruits[i]` represents the **quantity** of the `ith` type of fruit, and
    `baskets[j]` represents the **capacity** of the `jth` basket.

    From left to right, place the fruits according to these rules:

    * Each fruit type must be placed in the **leftmost available basket** with a
    capacity **greater than or equal** to the quantity of that fruit type.

    * Each basket can hold **only one** type of fruit.

    * If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

    Return the number of fruit types that remain unplaced after all possible allocations
    are made."""

    def num_of_unplaced_fruits(self, fruits: list[int], baskets: list[int]) -> int: ...

    numOfUnplacedFruits = num_of_unplaced_fruits
