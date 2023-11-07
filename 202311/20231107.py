# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/


class Solution:
    """1921. Eliminate Maximum Number of Monsters

    You are playing a video game where you are defending your city from a group of `n`
    monsters. You are given a **0-indexed** integer array `dist` of size `n`, where
    `dist[i]` is the **initial distance** in kilometers of the `ith` monster from the
    city.

    The monsters walk toward the city at a **constant** speed. The speed of each monster
    is given to you in an integer array `speed` of size `n`, where `speed[i]` is the
    speed of the `ith` monster in kilometers per minute.

    You have a weapon that, once fully charged, can eliminate a **single** monster.
    However, the weapon takes **one minute** to charge. The weapon is fully charged at
    the very start.

    You lose when any monster reaches your city. If a monster reaches the city at the
    exact moment the weapon is fully charged, it counts as a **loss**, and the game ends
    before you can use your weapon.

    Return *the **maximum** number of monsters that you can eliminate before you lose,
    or* `n` *if you can eliminate all the monsters before they reach the city.*
    """

    def eliminate_maximum(self, dist: list[int], speed: list[int]) -> int:
        """The maximum number of monsters you can eliminate before you lose.

        Args:
            dist: A list of initial distances of monsters from the city.
            speed: A list of speeds of monsters in kilometers per minute.

        Returns:
            The **maximum** number of monsters that you can eliminate before you lose,
            or `n` if you can eliminate all the monsters before they reach the city.
        """
        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]

        # Sort the monsters by their time it takes for them to reach the city.
        time_to_city.sort()

        for i in range(len(time_to_city)):
            # If weapon is charged before the monster reaches the city, the monster is
            # eliminated.
            if time_to_city[i] <= i:
                return i

        return len(dist)

    eliminateMaximum = eliminate_maximum
