# https://leetcode.com/problems/my-calendar-i/
from bisect import bisect_left, insort_left


class MyCalendar:
    """729. My Calendar I

    You are implementing a program to use as your calendar. We can add a new event if
    adding the event will not cause a **double booking**.

    A **double booking** happens when two events have some non\\-empty intersection
    (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers `start` and `end` that represents
    a booking on the half\\-open interval `[start, end)`, the range of real numbers `x`
    such that `start <= x < end`.

    Implement the `MyCalendar` class:

    * `MyCalendar()` Initializes the calendar object.

    * `boolean book(int start, int end)` Returns `true` if the event can be added to the
    calendar successfully without causing a **double booking**. Otherwise, return
    `false` and do not add the event to the calendar.


    Your MyCalendar object will be instantiated and called as such:
    obj = MyCalendar()
    param_1 = obj.book(start,end)

    """

    def __init__(self):
        # List to store tuples of (start, end) for each booking
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Find the position where 'start' could be inserted
        idx = bisect_left(self.bookings, (start, float("inf")))

        # Check for overlap with the previous event if it exists
        if idx > 0 and self.bookings[idx-1][1] > start:
            return False

        # Check for overlap with the next event if it exists
        if idx < len(self.bookings) and end > self.bookings[idx][0]:
            return False

        # If no overlaps found, add the booking
        self.bookings.insert(idx, (start, end))
        return True