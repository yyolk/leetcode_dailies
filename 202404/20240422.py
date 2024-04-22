# https://leetcode.com/problems/open-the-lock/


class Solution:
    """752. Open the Lock

    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
    `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and
    wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each
    move consists of turning one wheel one slot.

    The lock initially starts at `'0000'`, a string representing the state of the 4
    wheels.

    You are given a list of `deadends` dead ends, meaning if the lock displays any of
    these codes, the wheels of the lock will stop turning and you will be unable to open
    it.

    Given a `target` representing the value of the wheels that will unlock the lock,
    return the minimum total number of turns required to open the lock, or -1 if it is
    impossible.

    """

    def open_lock(self, deadends: list[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                for d in (-1, 1):
                    yield node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]

        dead = set(deadends)
        visited = set()
        queue = [('0000', 0)]

        while queue:
            node, depth = queue.pop(0)
            if node == target:
                return depth
            if node in visited or node in dead:
                continue
            visited.add(node)
            queue.extend((n, depth + 1) for n in neighbors(node))

        return -1

    openLock = open_lock
