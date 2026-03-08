# https://leetcode.com/problems/find-unique-binary-string

class Solution:
    """1980. Find Unique Binary String
    
    Given an array of strings nums containing n unique binary strings each of length
    n, return a binary string of length n that does not appear in nums. If there are
    multiple answers, you may return any of them.
    """
    def find_different_binary_string(self, nums: list[str]) -> str:
        # Create a set for O(1) lookups (though n ≤ 16 so even list would work)
        seen = set(nums)
        
        n = len(nums)
        
        # Use diagonal flip approach: differ from each string at position i
        # Guarantees the result differs from nums[i] at index i
        result = []
        for i in range(n):
            # Flip the i-th bit of the i-th string
            current_bit = nums[i][i]
            result.append("1" if current_bit == "0" else "0")
        
        return "".join(result)

    findDifferentBinaryString = find_different_binary_string