# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution:
    """1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
    
    A decimal number is called deci-binary if each of its digits is either 0 or 1
    without any leading zeros. For example, 101 and 1100 are deci-binary, while
    112 and 3001 are not.
    
    Given a string n that represents a positive decimal integer, return the
    minimum number of positive deci-binary numbers needed so that they sum up
    to n.
    """
    def min_partitions(self, n: str) -> int:
        # answer is max digit in n: each deci-binary contributes at most 1
        # per position and max digit <=9 ensures no carries when summing
        return int(max(n))

    minPartitions = min_partitions