# https://leetcode.com/problems/seat-reservation-manager/
import heapq


class SeatManager:
    """
    Design a system that manages the reservation state of n seats that are numbered from
    `1` to `n`.

    Implement the `SeatManager` class:

    * `SeatManager(int n)` Initializes a `SeatManager` object that will manage `n`
    seats numbered from 1 to n. All seats are initially available.
    * `int reserve()` Fetches the **smallest-numbered** unreserved seat, reserves it,
    and returns its number.
    * `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

    Your SeatManager object will be instantiated and called as such:

        obj = SeatManager(n)
        param_1 = obj.reserve()
        obj.unreserve(seatNumber)
    """

    def __init__(self, n: int):
        # Initialize the available_seats list with seat numbers from 1 to n.
        self.available_seats = list(range(1, n + 1))
        # Convert it into a min-heap.
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        if self.available_seats:
            # Pop the smallest available seat number from the min-heap and return it.
            seat_number = heapq.heappop(self.available_seats)
            return seat_number

    def unreserve(self, seat_number: int):
        # Push the unreserved seat number back into the min-heap to maintain the order.
        heapq.heappush(self.available_seats, seat_number)
