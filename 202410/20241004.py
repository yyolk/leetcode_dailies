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

    def divide_players(self, skill: list[int]) -> int:
        n = len(skill)
        if n % 2 != 0:
            return -1  # If the length is not even, we can't make pairs
        
        # Sort the skill list
        skill.sort()
        
        # The target sum for each team
        target_sum = skill[0] + skill[-1]
        
        chemistry_sum = 0
        
        # Iterate over half of the list since we are making pairs
        for i in range(n // 2):
            # Check if the current pair sums to the target
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1  # If any pair does not match the target sum, return -1
            
            # Calculate chemistry for this pair
            chemistry_sum += skill[i] * skill[n - 1 - i]

        return chemistry_sum

    dividePlayers = divide_players
