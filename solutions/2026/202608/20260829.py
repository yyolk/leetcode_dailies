# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/


class Solution:
    """2948. Make Lexicographically Smallest Array by Swapping Elements

    You are given a **0-indexed** array of **positive** integers `nums` and a
    **positive** integer `limit`.

    In one operation, you can choose any two indices `i` and `j` and swap `nums[i]` and
    `nums[j]` **if** `|nums[i] - nums[j]| <= limit`.

    Return *the **lexicographically smallest array** that can be obtained by performing
    the operation any number of times*.

    An array `a` is lexicographically smaller than an array `b` if in the first position
    where `a` and `b` differ, array `a` has an element that is less than the
    corresponding element in `b`. For example, the array `[2,10,3]` is lexicographically
    smaller than the array `[10,2,3]` because they differ at index `0` and `2 < 10`.

    Constraints:

    * `1 <= nums.length <= 105`

    * `1 <= nums[i] <= 109`

    * `1 <= limit <= 109`
    """

    def lexicographically_smallest_array(
        self, nums: list[int], limit: int
    ) -> list[int]:
        n = len(nums)
        # Pair each value with its original index, then sort by value.
        arr = sorted(zip(nums, range(n)))
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            # Grow the group while consecutive sorted values differ by at most limit.
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
            # Within a group any permutation is reachable; place sorted values
            # into the sorted original indices for the lexicographically smallest result.
            idx = sorted(k for _, k in arr[i:j])
            for k, (x, _) in zip(idx, arr[i:j]):
                ans[k] = x
            i = j
        return ans

    lexicographicallySmallestArray = lexicographically_smallest_array
