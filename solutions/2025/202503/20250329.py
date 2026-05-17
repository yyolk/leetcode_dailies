# https://leetcode.com/problems/apply-operations-to-maximize-score/
MOD = 10**9 + 7


class Solution:
    """2818. Apply Operations to Maximize Score

    You are given an array `nums` of `n` positive integers and an integer `k`.

    Initially, you start with a score of `1`. You have to maximize your score by
    applying the following operation at most `k` times:

    * Choose any **non-empty** subarray `nums[l, ..., r]` that you haven't chosen
    previously.

    * Choose an element `x` of `nums[l, ..., r]` with the highest **prime score**. If
    multiple such elements exist, choose the one with the smallest index.

    * Multiply your score by `x`.

    Here, `nums[l, ..., r]` denotes the subarray of `nums` starting at index `l` and
    ending at the index `r`, both ends being inclusive.

    The **prime score** of an integer `x` is equal to the number of distinct prime
    factors of `x`. For example, the prime score of `300` is `3` since `300 = 2 * 2 * 3
    * 5 * 5`.

    Return *the **maximum possible score** after applying at most* `k` *operations*.

    Since the answer may be large, return it modulo `109 + 7`."""

    def maximum_score(self, nums: list[int], k: int) -> int:
        # Calculate the length of the input array
        array_length = len(nums)

        # Determine the upper limit for prime number calculations based on the maximum value in nums
        upper_limit = max(nums) + 1

        # Initialize a boolean list to identify prime numbers up to the upper limit
        is_prime = [True] * upper_limit
        is_prime[0] = is_prime[1] = False

        # Initialize a list to store the prime score (number of distinct prime factors) for each number
        prime_score = [0] * upper_limit

        # Use the Sieve of Eratosthenes to calculate prime scores for all numbers up to upper_limit
        for i in range(2, upper_limit):
            if is_prime[i]:
                for j in range(i, upper_limit, i):
                    # Increment the prime score for each multiple of the prime number i
                    prime_score[j] += 1
                    # Mark the multiple as non-prime
                    is_prime[j] = False

        # Initialize a list to store the index of the next greater prime score element
        next_greater_index = [array_length] * array_length
        stack = []

        # Compute the next greater prime score element index for each position from right to left
        for i in range(array_length - 1, -1, -1):
            # Remove elements from the stack with a lower or equal prime score
            while stack and prime_score[nums[i]] >= prime_score[nums[stack[-1]]]:
                stack.pop()
            # Set the next greater index; use array_length if no greater element exists
            next_greater_index[i] = stack[-1] if stack else array_length
            # Add the current index to the stack
            stack.append(i)

        # Initialize a list to store the index of the previous greater or equal prime score element
        prev_greater_or_equal_index = [-1] * array_length
        stack = []

        # Compute the previous greater or equal prime score element index for each position from left to right
        for i in range(array_length):
            # Remove elements from the stack with a strictly lower prime score
            while stack and prime_score[nums[i]] > prime_score[nums[stack[-1]]]:
                stack.pop()
            # Set the previous greater or equal index; use -1 if no such element exists
            prev_greater_or_equal_index[i] = stack[-1] if stack else -1
            # Add the current index to the stack
            stack.append(i)

        # Initialize the result variable to store the maximum score
        result = 1

        # Create a list of tuples containing each number and its original index
        number_index_tuples = [[nums[i], i] for i in range(array_length)]

        # Sort the tuples in descending order based on the number value
        number_index_tuples.sort(reverse=True)

        # Iterate through the sorted list of number-index pairs to compute the maximum score
        for number, index in number_index_tuples:
            # Calculate the maximum number of operations possible for this number based on its subarray range
            operations = min(
                (index - prev_greater_or_equal_index[index])
                * (next_greater_index[index] - index),
                k,
            )

            # Update the result by multiplying with the number raised to the power of operations, modulo MOD
            result = (result * self.pow(number, operations)) % MOD

            # Reduce the remaining operations count
            k -= operations

            # If no operations remain, return the computed result
            if k == 0:
                return result

        # Return the final maximum score after all possible operations
        return result

    def pow(self, base: int, exponent: int) -> int:
        # Initialize the result for the power computation
        power_result = 1

        # Compute base^exponent efficiently using exponentiation by squaring
        while exponent > 0:
            # If the exponent is odd, multiply the result by the base
            if exponent % 2 == 1:
                power_result = (power_result * base) % MOD
            # Square the base for the next iteration
            base = (base * base) % MOD
            # Halve the exponent
            exponent //= 2

        # Return the computed power modulo MOD
        return power_result

    maximumScore = maximum_score
