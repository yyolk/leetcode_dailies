# https://leetcode.com/problems/assign-cookies/


class Solution:
    """455. Assign Cookies

    Assume you are an awesome parent and want to give your children some cookies. But,
    you should give each child at most one cookie.

    Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that
    the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >=
    g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be
    content. Your goal is to maximize the number of your content children and output the
    maximum number.
    """

    def find_content_children(self, g: list[int], s: list[int]) -> int:
        # Step 1: Sort the greed factors and cookie sizes
        g.sort()
        s.sort()

        # Step 2: Initialize pointers and count variable
        i, j, count = 0, 0, 0

        # Step 3-6: Iterate through both arrays and assign cookies to children
        while i < len(g) and j < len(s):
            # Step 4: If a suitable cookie is found, assign it to the child
            if s[j] >= g[i]:
                count += 1
                i += 1  # Move to the next child
            j += 1  # Move to the next cookie

        # Step 7: Return the maximum number of content children
        return count

    findContentChildren = find_content_children
