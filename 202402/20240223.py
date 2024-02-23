# https://leetcode.com/problems/cheapest-flights-within-k-stops/


class Solution:
    """787. Cheapest Flights Within K Stops

    There are `n` cities connected by some number of flights. You are given an array
    `flights` where `flights[i] = [fromi, toi, pricei]` indicates that there is a flight
    from city `fromi` to city `toi` with cost `pricei`.

    You are also given three integers `src`, `dst`, and `k`, return ***the cheapest
    price** from* `src` *to* `dst` *with at most* `k` *stops.* If there is no such
    route, return`-1`.

    """

    def find_cheapest_price(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int: ...

    findCheapestPrice = find_cheapest_price
