# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

from collections import Counter


class Solution:
    """3020. Find the Maximum Number of Elements in Subset

    You are given an array of positive integers nums. You need to select a
    subset of nums which satisfies: place selected elements in array following
    [x, x^2, x^4, ..., x^{k/2}, x^k, x^{k/2}, ..., x^4, x^2, x] where k is
    any non-negative power of 2. E.g. [2,4,16,4,2] and [3,9,3] valid;
    [2,4,8,4,2] invalid. Return the maximum number of elements in such subset.
    """

    def maximum_length(self, nums: list[int]) -> int:
        count = Counter(nums)
        # 1 squares to itself so any odd-length sequence of 1s is valid
        ans = 0
        if 1 in count:
            c1 = count[1]
            ans = c1 if c1 % 2 == 1 else c1 - 1
        for num in count:
            if num == 1:
                continue
            length = 0
            x = num
            # greedily add 2 per valid side level (requires >=2) and square
            while count.get(x, 0) >= 2:
                length += 2  # symmetric pair positions filled
                x = x * x
            # use final x as center (+1) or fallback: demote last level to center (-1)
            length += 1 if count.get(x, 0) >= 1 else -1
            if length > ans:
                ans = length
        return ans

    maximumLength = maximum_length
