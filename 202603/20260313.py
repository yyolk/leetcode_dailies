# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero

import math

class Solution:
    """3296. Minimum Number of Seconds to Make Mountain Height Zero
    
    You are given an integer mountainHeight denoting the height of a mountain.
    You are also given an integer array workerTimes representing the work time of
    workers in seconds. The workers work simultaneously to reduce the height of
    the mountain. For worker i: To decrease the mountain's height by x, it takes
    workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For
    example: To reduce the height of the mountain by 1, it takes workerTimes[i]
    seconds. To reduce the height of the mountain by 2, it takes
    workerTimes[i] + workerTimes[i] * 2 seconds, and so on. Return an integer
    representing the minimum number of seconds required for the workers to make
    the height of the mountain 0.
    """
    def min_number_of_seconds(self, mountain_height: int, worker_times: list[int]) -> int:
        def get_reduced_height(time: int) -> int:
            # Total height reducible in `time` seconds by all workers
            total = 0
            for w in worker_times:
                k = time // w
                # max x where x*(x+1)//2 <= k (exact via isqrt)
                x = (-1 + math.isqrt(1 + 8 * k)) // 2
                total += x
            return total

        left = 0
        # tight upper bound: fastest worker alone does all height
        right = min(worker_times) * mountain_height * (mountain_height + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if get_reduced_height(mid) < mountain_height:
                left = mid + 1
            else:
                right = mid
        return left

    minNumberOfSeconds = min_number_of_seconds