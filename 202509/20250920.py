# https://leetcode.com/problems/implement-router/
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right


class Router:
    """3827. Implement Router

    Design a data structure that can efficiently manage data packets in a network
    router. Each data packet consists of the following attributes:

    * `source`: A unique identifier for the machine that generated the packet.

    * `destination`: A unique identifier for the target machine.

    * `timestamp`: The time at which the packet arrived at the router.

    Implement the `Router` class:

    `Router(int memory_limit)`: Initializes the Router object with a fixed memory limit.

    * `memory_limit` is the **maximum** number of packets the router can store at any
    given time.

    * If adding a new packet would exceed this limit, the **oldest** packet must be
    removed to free up space.

    `bool addPacket(int source, int destination, int timestamp)`: Adds a packet with the
    given attributes to the router.

    * A packet is considered a duplicate if another packet with the same `source`,
    `destination`, and `timestamp` already exists in the router.

    * Return `true` if the packet is successfully added (i.e., it is not a duplicate);
    otherwise return `false`.

    `int[] forwardPacket()`: Forwards the next packet in FIFO (First In First Out)
    order.

    * Remove the packet from storage.

    * Return the packet as an array `[source, destination, timestamp]`.

    * If there are no packets to forward, return an empty array.

    `int getCount(int destination, int start_time, int end_time)`:

    * Returns the number of packets currently stored in the router (i.e., not yet
    forwarded) that have the specified destination and have timestamps in the inclusive
    range `[start_time, end_time]`.

    **Note** that queries for `addPacket` will be made in increasing order of
    `timestamp`.


    Your Router object will be instantiated and called as such:
        obj = Router(memory_limit)
        param_1 = obj.addPacket(source,destination,timestamp)
        param_2 = obj.forwardPacket()
        param_3 = obj.getCount(destination,start_time,end_time)
    """

    def __init__(self, memory_limit: int):
        # Initialize memory limit
        self.memory_limit = memory_limit
        # Deque to maintain FIFO order of packets
        self.packets = deque()
        # Set for quick duplicate checks
        self.packet_set = set()
        # Dict of destination to list of timestamps (historical)
        self.packet_lists = defaultdict(list)
        # Dict of destination to current start index in the list
        self.start_indices = defaultdict(int)

    def add_packet(self, source: int, destination: int, timestamp: int) -> bool:
        # Key for duplicate check
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False
        # If at memory limit, remove oldest packet
        if len(self.packets) == self.memory_limit:
            s, d, t = self.packets.popleft()
            self.packet_set.remove((s, d, t))
            self.start_indices[d] += 1
        # Add new packet
        self.packets.append((source, destination, timestamp))
        self.packet_set.add(key)
        self.packet_lists[destination].append(timestamp)
        return True

    addPacket = add_packet

    def forward_packet(self) -> list[int]:
        if not self.packets:
            return []
        # Remove and return oldest packet
        s, d, t = self.packets.popleft()
        self.packet_set.remove((s, d, t))
        self.start_indices[d] += 1
        return [s, d, t]

    forwardPacket = forward_packet

    def get_count(self, destination: int, start_time: int, end_time: int) -> int:
        if destination not in self.packet_lists:
            return 0
        l = self.packet_lists[destination]
        start_idx = self.start_indices[destination]
        if start_idx >= len(l):
            return 0
        # Find left index for >= start_time
        idx_left = bisect_left(l, start_time)
        # Find right index for > end_time
        idx_right = bisect_right(l, end_time)
        # Adjust for active suffix starting at start_idx
        count = max(0, idx_right - max(idx_left, start_idx))
        return count

    getCount = get_count
