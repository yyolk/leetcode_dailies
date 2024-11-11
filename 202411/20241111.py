# https://leetcode.com/problems/prime-subtraction-operation/


class Solution:
    """2601. Prime Subtraction Operation

    You are given a **0\\-indexed** integer array `nums` of length `n`.

    You can perform the following operation as many times as you want:

    * Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly
    less than** `nums[i]`, then subtract `p` from `nums[i]`.

    Return *true if you can make `nums` a strictly increasing array using the above
    operation and false otherwise.*

    A **strictly increasing array** is an array whose each element is strictly greater
    than its preceding element.

    """

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_sub_operation(self, nums: list[int]) -> bool:
        # Process each number in the array
        for i in range(len(nums)):
            # Calculate the upper bound for subtraction
            bound = nums[0] if i == 0 else nums[i] - nums[i - 1]
            
            # If bound is not positive, sequence is impossible
            if bound <= 0:
                return False
            
            # Find the largest prime number less than bound
            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if self.is_prime(j):
                    largest_prime = j
                    break
            
            # Subtract the largest prime from current number
            nums[i] -= largest_prime
        
        return True

    primeSubOperation = prime_sub_operation
