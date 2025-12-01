# https://leetcode.com/problems/maximum-running-time-of-n-computers/


class Solution:
    """2141. Maximum Running Time of N Computers

    You have n computers. You are given the integer n and a 0-indexed
    integer array batteries where the ith battery can run a computer for
    batteries[i] minutes. You are interested in running all n computers
    simultaneously using the given batteries.

    Initially, you can insert at most one battery into each computer. After
    that and at any integer time moment, you can remove a battery from a
    computer and insert another battery any number of times. The inserted
    battery can be a totally new battery or a battery from another
    computer. You may assume that the removing and inserting processes take
    no time.

    Note that the batteries cannot be recharged.

    Return the maximum number of minutes you can run all the n computers
    simultaneously.
    """
    def max_run_time(self, n: int, batteries: list[int]) -> int:
        # Compute total battery capacity for upper bound on binary search
        total = sum(batteries)
        # Binary search bounds: low=0, high=total//n (max possible t)
        low, high = 0, total // n

        # Helper function to check if t is achievable
        def can_achieve(t: int) -> bool:
            # Sum of min(b, t) for all batteries: total computer-minutes up to t
            s = 0
            for b in batteries:
                s += min(b, t)
                # Early exit if already sufficient
                if s >= n * t:
                    return True
            # Check if total >= n * t
            return s >= n * t

        # Binary search for largest t where can_achieve(t) is True
        while low < high:
            # Bias towards high for upper mid
            mid = (low + high + 1) // 2
            if can_achieve(mid):
                low = mid
            else:
                high = mid - 1
        # low is the maximum achievable t
        return low

    maxRunTime = max_run_time