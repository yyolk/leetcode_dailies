# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/


class Solution:
    """2491. Divide Players Into Teams of Equal Skill

    You are given a positive integer array `skill` of **even** length `n` where
    `skill[i]` denotes the skill of the `ith` player. Divide the players into `n / 2`
    teams of size `2` such that the total skill of each team is **equal**.

    The **chemistry** of a team is equal to the **product** of the skills of the players
    on that team.

    Return *the sum of the **chemistry** of all the teams, or return* `-1` *if there is
    no way to divide the players into teams such that the total skill of each team is
    equal.*

    """

    def divide_players(self, skill: list[int]) -> int: ...

    dividePlayers = divide_players
