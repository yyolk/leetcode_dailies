# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class Solution:
    """3739. Count Subarrays With Majority Element II

    You are given an integer array nums and an integer target. Return the number of
    subarrays of nums in which target is the majority element. The majority element
    of a subarray is the element that appears strictly more than half of the times
    in that subarray.

    Constraints:
    * 1 <= nums.length <= 10**5
    * 1 <= nums[i] <= 10**9
    * 1 <= target <= 10**9
    """
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # +1 if == target else -1; prefix sum s = 2*target_count - length
        # s > 0 iff target strictly > length/2
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == target else -1)
        # compress all prefix values to ranks 1..m
        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        ft = [0] * (m + 2)
        def update(x):
            # add freq at rank x
            while x <= m:
                ft[x] += 1
                x += x & -x
        def query(x):
            # count of all ranks 1..x i.e. values <= current
            res = 0
            while x > 0:
                res += ft[x]
                x -= x & -x
            return res
        ans = 0
        # seed prefix[0] = 0
        update(rank[prefix[0]])
        for j in range(1, n + 1):
            # number of prior left where prefix[left] < prefix[j]
            ans += query(rank[prefix[j]] - 1)
            update(rank[prefix[j]])
        return ans

    countMajoritySubarrays = count_majority_subarrays