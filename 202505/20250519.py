# https://leetcode.com/problems/type-of-triangle/


class Solution:
    """3024. Type of Triangle

    You are given a **0-indexed** integer array `nums` of size `3` which can form the
    sides of a triangle.

    * A triangle is called **equilateral** if it has all sides of equal length.

    * A triangle is called **isosceles** if it has exactly two sides of equal length.

    * A triangle is called **scalene** if all its sides are of different lengths.

    Return *a string representing* *the type of triangle that can be formed* *or*
    `"none"` *if it **cannot** form a triangle.*"""

    def triangle_type(self, nums: list[int]) -> str:
        match nums:
            # Check if any side is non-positive (zero or negative). Triangles require positive side lengths.
            case [x, y, z] if x <= 0 or y <= 0 or z <= 0:
                return "none"

            # Check the triangle inequality: the sum of any two sides must be greater than the third side.
            case [x, y, z] if x + y <= z or x + z <= y or y + z <= x:
                return "none"

            # Check if all three sides are equal, which defines an equilateral triangle.
            case [x, y, z] if x == y == z:
                return "equilateral"

            # Check if exactly two sides are equal, which defines an isosceles triangle.
            case [x, y, z] if x == y or y == z or x == z:
                return "isosceles"

            # If all sides are different and form a valid triangle, it is a scalene triangle.
            case _:
                return "scalene"

    triangleType = triangle_type
