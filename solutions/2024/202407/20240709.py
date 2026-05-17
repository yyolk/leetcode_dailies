# https://leetcode.com/problems/average-waiting-time/


class Solution:
    """1701. Average Waiting Time

    There is a restaurant with a single chef. You are given an array `customers`, where
    `customers[i] = [arrivali, timei]:`

    * `arrivali` is the arrival time of the `ith` customer. The arrival times are sorted
    in **non-decreasing** order.

    * `timei` is the time needed to prepare the order of the `ith` customer.

    When a customer arrives, he gives the chef his order, and the chef starts preparing
    it once he is idle. The customer waits till the chef finishes preparing his order.
    The chef does not prepare food for more than one customer at a time. The chef
    prepares food for customers **in the order they were given in the input**.

    Return *the **average** waiting time of all customers*. Solutions within `10-5` from
    the actual answer are considered accepted.

    """

    def average_waiting_time(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_waiting_time = 0

        for arrival, time in customers:
            # If the chef is idle, start the order when the customer arrives
            if current_time < arrival:
                current_time = arrival

            # Calculate the waiting time for the current customer
            waiting_time = current_time - arrival + time

            # Update the current time by adding the time needed to prepare the order
            current_time += time

            # Accumulate the total waiting time
            total_waiting_time += waiting_time

        # Calculate and return the average waiting time
        return total_waiting_time / len(customers)

    averageWaitingTime = average_waiting_time
