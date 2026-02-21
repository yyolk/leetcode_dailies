# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation


class Solution:
    """762. Prime Number of Set Bits in Binary Representation
    
    Given two integers left and right, return the count of numbers in the
    inclusive range [left, right] having a prime number of set bits in their
    binary representation. Recall that the number of set bits an integer has
    is the number of 1's present when written in binary.
    
    For example, 21 written in binary is 10101, which has 3 set bits.
    """
    def count_prime_set_bits(self, left: int, right: int) -> int:
        # Precompute primes (max set bits for <=10^6 is 20; include up to 31)
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        count = 0
        for num in range(left, right + 1):
            # Count set bits via binary string (fast and readable)
            bits = bin(num).count("1")
            # Increment only for prime bit counts
            if bits in primes:
                count += 1
        return count

    countPrimeSetBits = count_prime_set_bits