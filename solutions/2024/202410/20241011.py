# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
import heapq


class Solution:
    """1942. The Number of the Smallest Unoccupied Chair

    There is a party where `n` friends numbered from `0` to `n - 1` are attending. There
    is an **infinite** number of chairs in this party that are numbered from `0` to
    `infinity`. When a friend arrives at the party, they sit on the unoccupied chair
    with the **smallest number**.

    * For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they
    will sit on chair number `2`.

    When a friend leaves the party, their chair becomes unoccupied at the moment they
    leave. If another friend arrives at that same moment, they can sit in that chair.

    You are given a **0\\-indexed** 2D integer array `times` where `times[i] = [arrivali,
    leavingi]`, indicating the arrival and leaving times of the `ith` friend
    respectively, and an integer `target_friend`. All arrival times are **distinct**.

    Return *the **chair number** that the friend numbered* `target_friend` *will sit
    on*.

    """

    def smallest_chair(self, times: list[list[int]], target_friend: int) -> int:
        # Convert target friend to index
        target_friend_index = target_friend

        # Add chair index to each time for tracking who sits where
        for i, (arrival, leaving) in enumerate(times):
            # [arrival, leaving, friend_index]
            times[i].append(i)

        # Sort by arrival time
        times.sort(key=lambda x: x[0])

        # Heap to keep track of available chairs (by chair number)
        available_chairs = [i for i in range(len(times))]
        heapq.heapify(available_chairs)

        # Heap to keep track of when chairs will be freed (time, chair)
        occupied_chairs = []

        for arrival, leaving, friend_index in times:
            # Free up all chairs that are vacated by now
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)

            # Assign chair
            chair = heapq.heappop(available_chairs)
            if friend_index == target_friend_index:
                return chair

            # Schedule this chair to be freed
            heapq.heappush(occupied_chairs, (leaving, chair))

        # This line should never be reached given the problem's constraints
        # Error case, but should not occur if input is valid
        return -1

    smallestChair = smallest_chair
