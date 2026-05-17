# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
from collections import Counter


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
        # Count all the losing matches, by their loser
        loss_count = Counter(loser for _, loser in matches)

        # Collect all players who have played at least one match
        all_players = set(player for match in matches for player in match)

        # Create lists of players
        zero_loss = [player for player in all_players if loss_count.get(player, 0) == 0]
        lost_one_match = [player for player, count in loss_count.items() if count == 1]

        # Sort the lists
        zero_loss.sort()
        lost_one_match.sort()

        return [zero_loss, lost_one_match]

    findWinners = find_winners
