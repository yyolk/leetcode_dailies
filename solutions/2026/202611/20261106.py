# https://leetcode.com/problems/count-zero-request-servers/


class Solution:
    """2747. Count Zero Request Servers

    You are given an integer `n` denoting the total number of servers and a **2D**
    **0-indexed** integer array `logs`, where `logs[i] = [server_id, time]` denotes that
    the server with id `server_id` received a request at time `time`.

    You are also given an integer `x` and a **0-indexed** integer array `queries`.

    Return *a **0-indexed** integer array* `arr` *of length* `queries.length` *where*
    `arr[i]` *represents the number of servers that **did not receive** any requests
    during the time interval* `[queries[i] - x, queries[i]]`.

    Note that the time intervals are inclusive.

    Constraints:

    * `1 <= n <= 105`

    * `1 <= logs.length <= 105`

    * `1 <= queries.length <= 105`

    * `logs[i].length == 2`

    * `1 <= logs[i][0] <= n`

    * `1 <= logs[i][1] <= 106`

    * `1 <= x <= 105`

    * `x < queries[i] <= 106`"""

    def count_servers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        """...

        Proposed solution ...

        Args:
            n (int): ...
            logs (list of list of int): ...
            x (int): ...
            queries (list of int): ...

        Returns:
            list of int: ..."""
        ...

    countServers = count_servers
