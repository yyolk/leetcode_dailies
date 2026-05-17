# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution:
    """1674. Minimum Moves to Make Array Complementary

    You are given an integer array nums of even length n and an integer limit. In
    one move, you can replace any integer from nums with another integer between 1
    and limit, inclusive.

    The array nums is complementary if for all indices i (0-indexed), nums[i] +
    nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is
    complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

    Return the minimum number of moves required to make nums complementary.
    """
    def min_moves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        # max possible S is 2 * limit
        max_s = 2 * limit
        # diff array for range updates on cover [minv+1, maxv+limit]
        diff = [0] * (max_s + 2)
        exact = [0] * (max_s + 2)
        # process each of the n/2 pairs
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            minv = min(a, b)
            maxv = max(a, b)
            # S in [minv+1, maxv+limit] allows cost <=1
            lo = minv + 1
            r = maxv + limit
            diff[lo] += 1
            diff[r + 1] -= 1
            # cost 0 at exact sum
            s = a + b
            exact[s] += 1
        # compute cover counts via prefix
        cover = [0] * (max_s + 2)
        curr = 0
        for s in range(len(cover)):
            curr += diff[s]
            cover[s] = curr
        # find max (cover[S] + exact[S])
        max_good = 0
        for s in range(2, max_s + 1):
            good = cover[s] + exact[s]
            if good > max_good:
                max_good = good
        # total moves: n - max_good (base cost 2 per pair)
        return n - max_good

    minMoves = min_moves