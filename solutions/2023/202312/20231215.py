# https://leetcode.com/problems/destination-city/


class Solution:
    """1436. Destination City

    You are given the array `paths`, where `paths[i] = [cityAi, cityBi]` means there
    exists a direct path going from `cityAi` to `cityBi`. *Return the destination city,
    that is, the city without any path outgoing to another city.*

    It is guaranteed that the graph of paths forms a line without any loop, therefore,
    there will be exactly one destination city.
    """

    def dest_city(self, paths: list[list[str]]) -> str:
        """Destination city.

        Args:
            paths: A list of paths.

        Returns:
            The destination city.
        """
        outgoing = set()
        incoming = set()

        # Iterate through the paths and record outgoing and incoming cities
        for path in paths:
            outgoing.add(path[0])
            incoming.add(path[1])

        # Find the destination city
        destination = incoming - outgoing

        # Convert the set to a list and return the destination city
        return list(destination)[0]

    destCity = dest_city
