# https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution:
    """3658. GCD of Odd and Even Sums
    
    You are given an integer n. Your task is to compute the GCD (greatest common
    divisor) of two values: * sumOdd: the sum of the smallest n positive odd
    numbers. * sumEven: the sum of the smallest n positive even numbers. Return
    the GCD of sumOdd and sumEven.
    Constraints: * 1 <= n <= 1000000000"""
    def gcd_of_odd_even_sums(self, n: int) -> int:
        # sum of first n odds: n**2
        # sum of first n evens: n*(n + 1)
        # gcd(n**2, n*(n + 1)) = n * gcd(n, n + 1) = n * 1 = n
        # since n and n+1 are always coprime
        return n

    gcdOfOddEvenSums = gcd_of_odd_even_sums
