# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/


class Solution:
    """3147. Taking Maximum Energy From the Mystic Dungeon

    In a mystic dungeon, `n` magicians are standing in a line. Each magician has an
    attribute that gives you energy. Some magicians can give you negative energy, which
    means taking energy from you.

    You have been cursed in such a way that after absorbing energy from magician `i`,
    you will be instantly transported to magician `(i + k)`. This process will be
    repeated until you reach the magician where `(i + k)` does not exist.

    In other words, you will choose a starting point and then teleport with `k` jumps
    until you reach the end of the magicians' sequence, **absorbing all the energy**
    during the journey.

    You are given an array `energy` and an integer `k`. Return the **maximum** possible
    energy you can gain.

    **Note** that when you are reach a magician, you *must* take energy from them,
    whether it is negative or positive energy."""

    def maximum_energy(self, energy: list[int], k: int) -> int:
        # Initialize the answer to the smallest possible integer
        ans = float('-inf')
        # Iterate over each possible residue class modulo k
        for r in range(k):
            # Collect the energy values for this residue class
            b = [energy[i] for i in range(r, len(energy), k)]
            # Get the length of this group
            m = len(b)
            # Skip if the group is empty
            if m == 0:
                continue
            # Compute the total sum of the group
            total = sum(b)
            # Initialize min_prefix to 0 (empty prefix)
            min_prefix = 0
            # Initialize current prefix sum
            current = 0
            # Compute prefixes up to m-1 and track the minimum
            for j in range(1, m):
                # Add the next element to the current prefix
                current += b[j - 1]
                # Update the minimum prefix
                min_prefix = min(min_prefix, current)
            # The max suffix sum for this group is total minus the min prefix
            max_group = total - min_prefix
            # Update the overall answer with this group's max
            ans = max(ans, max_group)
        # Return the maximum energy found
        return ans

    maximumEnergy = maximum_energy
