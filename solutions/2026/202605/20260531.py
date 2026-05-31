# https://leetcode.com/problems/destroying-asteroids/


class Solution:
    """2126. Destroying Asteroids

    You are given an integer mass, which represents the original mass of a planet.
    You are further given an integer array asteroids, where asteroids[i] is the mass
    of the ith asteroid.

    You can arrange for the planet to collide with the asteroids in any arbitrary
    order. If the mass of the planet is greater than or equal to the mass of the
    asteroid, the asteroid is destroyed and the planet gains the mass of the
    asteroid. Otherwise, the planet is destroyed.

    Return true if all asteroids can be destroyed. Otherwise, return false.
    """

    def asteroids_destroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort asteroids ascending: collide with smallest first to grow planet
        asteroids.sort()
        for asteroid in asteroids:
            # Cannot destroy this asteroid (or any remaining)
            if mass < asteroid:
                return False
            # Destroy and add mass to planet
            mass += asteroid
        return True

    asteroidsDestroyed = asteroids_destroyed
