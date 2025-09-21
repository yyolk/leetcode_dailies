# https://leetcode.com/problems/design-movie-rental-system/
from collections import defaultdict
from sortedcontainers import SortedList


class MovieRentingSystem:
    """2023. Design Movie Rental System

    You have a movie renting company consisting of `n` shops. You want to implement a
    renting system that supports searching for, booking, and returning movies. The
    system should also support generating a report of the currently rented movies.

    Each movie is given as a 2D integer array `entries` where `entries[i] = [shopi,
    moviei, pricei]` indicates that there is a copy of movie `moviei` at shop `shopi`
    with a rental price of `pricei`. Each shop carries **at most one** copy of a movie
    `moviei`.

    The system should support the following functions:

    * **Search**: Finds the **cheapest 5 shops** that have an **unrented copy** of a
    given movie. The shops should be sorted by **price** in ascending order, and in case
    of a tie, the one with the **smaller** `shopi` should appear first. If there are
    less than 5 matching shops, then all of them should be returned. If no shop has an
    unrented copy, then an empty list should be returned.

    * **Rent**: Rents an **unrented copy** of a given movie from a given shop.

    * **Drop**: Drops off a **previously rented copy** of a given movie at a given shop.

    * **Report**: Returns the **cheapest 5 rented movies** (possibly of the same movie
    ID) as a 2D list `res` where `res[j] = [shopj, moviej]` describes that the `jth`
    cheapest rented movie `moviej` was rented from the shop `shopj`. The movies in `res`
    should be sorted by **price** in ascending order, and in case of a tie, the one with
    the **smaller** `shopj` should appear first, and if there is still tie, the one with
    the **smaller** `moviej` should appear first. If there are fewer than 5 rented
    movies, then all of them should be returned. If no movies are currently being
    rented, then an empty list should be returned.

    Implement the `MovieRentingSystem` class:

    * `MovieRentingSystem(int n, int[][] entries)` Initializes the `MovieRentingSystem`
    object with `n` shops and the movies in `entries`.

    * `list<Integer> search(int movie)` Returns a list of shops that have an **unrented
    copy** of the given `movie` as described above.

    * `void rent(int shop, int movie)` Rents the given `movie` from the given `shop`.

    * `void drop(int shop, int movie)` Drops off a previously rented `movie` at the
    given `shop`.

    * `list<list<Integer>> report()` Returns a list of cheapest **rented** movies as
    described above.

    **Note:** The test cases will be generated such that `rent` will only be called if
    the shop has an **unrented** copy of the movie, and `drop` will only be called if
    the shop had **previously rented** out the movie.

    Your MovieRentingSystem object will be instantiated and called as such:
        obj = MovieRentingSystem(n, entries)
        param_1 = obj.search(movie)
        obj.rent(shop,movie)
        obj.drop(shop,movie)
        param_4 = obj.report()
    """

    def __init__(self, n: int, entries: list[list[int]]):
        # Store unrented movies: movie_id -> sorted list of (price, shop_id)
        self.unrented = defaultdict(SortedList)

        # Store price lookup: (shop_id, movie_id) -> price
        self.shop_and_movie_to_price = {}

        # Store currently rented movies: sorted list of (price, shop_id, movie_id)
        self.rented = SortedList()

        # Process initial entries
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.shop_and_movie_to_price[(shop, movie)] = price

    def search(self, movie: int) -> list[int]:
        # Return shop IDs from the first 5 (price, shop) tuples
        return [shop for _, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        # Get the price for this shop-movie combination
        price = self.shop_and_movie_to_price[(shop, movie)]

        # Remove from unrented inventory
        self.unrented[movie].remove((price, shop))

        # Add to rented inventory
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        # Get the price for this shop-movie combination
        price = self.shop_and_movie_to_price[(shop, movie)]

        # Add back to unrented inventory
        self.unrented[movie].add((price, shop))

        # Remove from rented inventory
        self.rented.remove((price, shop, movie))

    def report(self) -> list[list[int]]:
        # Return shop and movie IDs from the first 5 rented entries
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
