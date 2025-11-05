# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/


class Solution:
    """3321. Find X-Sum of All K-Long Subarrays II

    You are given an array nums of n integers and two integers k and x.

    The x-sum of an array is calculated by the following procedure:

    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements
    have the same number of occurrences, the element with the bigger value is
    considered more frequent.
    
    Calculate the sum of the resulting array.
    
    Note that if an array has less than x distinct elements, its x-sum is the sum
    of the array.

    Return an integer array answer of length n - k + 1 where answer[i] is the x-sum
    of the subarray nums[i..i + k - 1].
    """
    def find_x_sum(self, nums: list[int], k: int, x: int) -> list[int]:
        # Define function to add a value's current frequency tuple to the appropriate sorted list
        def add(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            # If top list exists and current is greater than the smallest in top, add to top
            if l and p > l[0]:
                nonlocal s
                s += p[0] * p[1]  # Add contribution to sum
                l.add(p)
            else:
                r.add(p)

        # Define function to remove a value's current frequency tuple from the sorted lists
        def remove(v: int):
            if cnt[v] == 0:
                return
            p = (cnt[v], v)
            # Check if in top list and remove if present, updating sum
            if p in l:
                nonlocal s
                s -= p[0] * p[1]  # Subtract contribution from sum
                l.remove(p)
            else:
                r.remove(p)

        # SortedList for top x elements (ascending order)
        l = SortedList()
        # SortedList for remaining elements (ascending order)
        r = SortedList()
        # Counter for frequencies in current window
        cnt = Counter()
        # Current x-sum
        s = 0
        # Length of nums
        n = len(nums)
        # Result array
        ans = [0] * (n - k + 1)
        # Process each element to build and slide the window
        for i, v in enumerate(nums):
            # Remove old frequency entry before increment
            remove(v)
            # Increment frequency
            cnt[v] += 1
            # Add new frequency entry
            add(v)
            # Compute window start
            j = i - k + 1
            if j < 0:
                continue
            # Move from remaining to top if top has less than x
            while r and len(l) < x:
                p = r.pop()  # Get largest from remaining
                l.add(p)
                s += p[0] * p[1]  # Update sum
            # Move from top to remaining if top has more than x
            while len(l) > x:
                p = l.pop(0)  # Get smallest from top
                s -= p[0] * p[1]  # Update sum
                r.add(p)
            # Record the current sum for this window
            ans[j] = s
            # Prepare to slide: remove old frequency of leaving element
            remove(nums[j])
            # Decrement frequency
            cnt[nums[j]] -= 1
            # Add back if frequency still positive
            add(nums[j])

        return ans

    findXSum = find_x_sum