# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

import bisect


class Solution:
    """1385. Find the Distance Value Between Two Arrays

    Given two integer arrays arr1 and arr2, and the integer d, return the
    distance value between the two arrays.

    The distance value is defined as the number of elements arr1[i] such that
    there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

    Constraints:

    * 1 <= arr1.length, arr2.length <= 500
    * -1000 <= arr1[i], arr2[j] <= 1000
    * 0 <= d <= 100
    """

    def find_the_distance_value(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort arr2 so we can binary-search for any value in [x - d, x + d].
        arr2.sort()
        count = 0
        for x in arr1:
            # First index where arr2[i] >= x - d.
            left = bisect.bisect_left(arr2, x - d)
            # If that element exists and is <= x + d, a close value is present.
            if left < len(arr2) and arr2[left] <= x + d:
                continue
            count += 1
        return count

    findTheDistanceValue = find_the_distance_value
