# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/


class Solution:
    """3494. Find the Minimum Amount of Time to Brew Potions

    You are given two integer arrays, `skill` and `mana`, of length `n` and `m`,
    respectively.

    In a laboratory, `n` wizards must brew `m` potions *in order*. Each potion has a
    mana capacity `mana[j]` and **must** pass through **all** the wizards sequentially
    to be brewed properly. The time taken by the `ith` wizard on the `jth` potion is
    `timeij = skill[i] * mana[j]`.

    Since the brewing process is delicate, a potion **must** be passed to the next
    wizard immediately after the current wizard completes their work. This means the
    timing must be *synchronized* so that each wizard begins working on a potion
    **exactly** when it arrives. \u200b

    Return the **minimum** amount of time required for the potions to be brewed
    properly."""

    def min_time(self, skill: list[int], mana: list[int]) -> int:
        # Calculate the sum of all wizard skills
        sum_skill = sum(skill)
        # Initialize the completion time for the first potion
        prev_wizard_done = sum_skill * mana[0]
        # Process each subsequent potion
        for j in range(1, len(mana)):
            # Set to the completion time of the last wizard on the previous potion
            prev_potion_done = prev_wizard_done
            # Iterate backwards over the wizards from second-to-last to first
            for i in range(len(skill) - 2, -1, -1):
                # Subtract the brewing time of the next wizard on the previous potion to get the completion time on current wizard
                prev_potion_done -= skill[i + 1] * mana[j - 1]
                # Update to the maximum of the current completion on previous potion or adjusted previous value
                prev_wizard_done = max(prev_potion_done, prev_wizard_done - skill[i] * mana[j])
            # Add the total brewing time for the current potion to get its completion time
            prev_wizard_done += sum_skill * mana[j]
        return prev_wizard_done        

    minTime = min_time
