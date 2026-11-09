# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

import heapq


class Solution:
    """1606. Find Servers That Handled Most Number of Requests

    You have `k` servers numbered from `0` to `k-1` that are being used to handle
    multiple requests simultaneously. Each server has infinite computational capacity
    but **cannot handle more than one request at a time**. The requests are assigned to
    servers according to a specific algorithm:

    * The `ith` (0-indexed) request arrives.

    * If all servers are busy, the request is dropped (not handled at all).

    * If the `(i % k)th` server is available, assign the request to that server.

    * Otherwise, assign the request to the next available server (wrapping around the
    list of servers and starting from 0 if necessary). For example, if the `ith` server
    is busy, try to assign the request to the `(i+1)th` server, then the `(i+2)th`
    server, and so on.

    You are given a **strictly increasing** array `arrival` of positive integers, where
    `arrival[i]` represents the arrival time of the `ith` request, and another array
    `load`, where `load[i]` represents the load of the `ith` request (the time it takes
    to complete). Your goal is to find the **busiest server(s)**. A server is considered
    **busiest** if it handled the most number of requests successfully among all the
    servers.

    Return *a list containing the IDs (0-indexed) of the **busiest server(s)***. You may
    return the IDs in any order.

    Constraints:

    * `1 <= k <= 105`

    * `1 <= arrival.length, load.length <= 105`

    * `arrival.length == load.length`

    * `1 <= arrival[i], load[i] <= 109`

    * `arrival` is **strictly increasing**.
    """

    def busiest_servers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap of busy servers ordered by end time: (end_time, server_id)
        busy: list[tuple[int, int]] = []
        # Min-heap of free servers by virtual index for circular preference
        free: list[int] = list(range(k))
        heapq.heapify(free)
        # Number of requests handled by each server
        counts = [0] * k

        for i, (arr_time, ld) in enumerate(zip(arrival, load)):
            # Release servers that have finished by the current arrival time
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                # Map back into the preferred circular order starting at i % k
                virtual = i + (server_id - i % k) % k
                heapq.heappush(free, virtual)
            if not free:
                # No server available; drop this request
                continue
            # Select the earliest preferred free server and normalize its id
            server_id = heapq.heappop(free) % k
            counts[server_id] += 1
            heapq.heappush(busy, (arr_time + ld, server_id))

        max_count = max(counts)
        return [sid for sid in range(k) if counts[sid] == max_count]

    busiestServers = busiest_servers
