# https://leetcode.com/problems/find-players-with-zero-or-one-losses/


class Solution:
    """2225. Find Players With Zero or One Losses

    You are given an integer array `matches` where `matches[i] = [winneri, loseri]`
    indicates that the player `winneri` defeated player `loseri` in a match.

    Return *a list* `answer` *of size* `2` *where:*

    * `answer[0]` is a list of all players that have **not** lost any matches.

    * `answer[1]` is a list of all players that have lost exactly **one** match.

    The values in the two lists should be returned in **increasing** order.

    **Note:**

    * You should only consider the players that have played **at least one** match.

    * The testcases will be generated such that **no** two matches will have the
    **same** outcome.
    """

    def find_winners(self, matches: list[list[int]]) -> list[list[int]]:
        ...

    findWinners = find_winners
