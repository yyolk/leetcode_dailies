# https://leetcode.com/problems/count-zero-request-servers/


class Solution:
    """2747. Count Zero Request Servers

    You are given an integer `n` denoting the total number of servers and a
    **2D** **0-indexed** integer array `logs`, where `logs[i] = [server_id,
    time]` denotes that the server with id `server_id` received a request at
    time `time`.

    You are also given an integer `x` and a **0-indexed** integer array
    `queries`.

    Return *a **0-indexed** integer array* `arr` *of length* `queries.length`
    *where* `arr[i]` *represents the number of servers that **did not receive**
    any requests during the time interval* `[queries[i] - x, queries[i]]`.

    Note that the time intervals are inclusive.

    Constraints:

    * `1 <= n <= 10**5`
    * `1 <= logs.length <= 10**5`
    * `1 <= queries.length <= 10**5`
    * `logs[i].length == 2`
    * `1 <= logs[i][0] <= n`
    * `1 <= logs[i][1] <= 10**6`
    * `1 <= x <= 10**5`
    * `x < queries[i] <= 10**6`
    """

    def count_servers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        # Sort logs by time so a sliding window can process them in order.
        logs.sort(key=lambda log: log[1])
        # Per-server request counts inside the current window and active count.
        count = [0] * (n + 1)
        active = 0
        left = right = 0
        ans = [0] * len(queries)
        # Process queries offline in increasing time order.
        for qi, q in sorted(enumerate(queries), key=lambda p: p[1]):
            # Include every log whose time is <= the query time.
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if count[server] == 0:
                    active += 1
                count[server] += 1
                right += 1
            # Exclude every log whose time is strictly before the window start.
            while left < len(logs) and logs[left][1] < q - x:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                left += 1
            # Servers that received no requests in [q - x, q].
            ans[qi] = n - active
        return ans

    countServers = count_servers
