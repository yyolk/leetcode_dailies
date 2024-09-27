# https://leetcode.com/problems/my-calendar-ii/


class MyCalendarTwo:
    """731. My Calendar II

    You are implementing a program to use as your calendar. We can add a new event if
    adding the event will not cause a **triple booking**.

    A **triple booking** happens when three events have some non\\-empty intersection
    (i.e., some moment is common to all the three events.).

    The event can be represented as a pair of integers `start` and `end` that represents
    a booking on the half\\-open interval `[start, end)`, the range of real numbers `x`
    such that `start <= x < end`.

    Implement the `MyCalendarTwo` class:

    * `MyCalendarTwo()` Initializes the calendar object.

    * `boolean book(int start, int end)` Returns `true` if the event can be added to the
    calendar successfully without causing a **triple booking**. Otherwise, return
    `false` and do not add the event to the calendar.

    Your MyCalendarTwo object will be instantiated and called as such:
        obj = MyCalendarTwo()
        param_1 = obj.book(start,end)
    """
    def __init__(self):
        # List to store all single bookings
        self.bookings = []
        # List to store overlaps (double bookings)
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new event overlaps with any existing double bookings
        for i, j in self.overlaps:
            if start < j and end > i:
                return False  # This would cause a triple booking

        # Check for overlap with single bookings to update overlaps
        for i, j in self.bookings:
            if start < j and end > i:
                # If there's an overlap, add to overlaps, but only the overlapping section
                self.overlaps.append((max(start, i), min(end, j)))

        # If we've made it this far, we can add this as a single booking
        self.bookings.append((start, end))
        return True