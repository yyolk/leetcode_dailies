# https://leetcode.com/problems/check-if-n-and-its-double-exist/


class Solution:
    """1346. Check If N and Its Double Exist

    Given an array `arr` of integers, check if there exist two indices `i` and `j` such
    that :

    * `i != j`

    * `0 <= i, j < arr.length`

    * `arr[i] == 2 * arr[j]`"""

    def check_if_exist(self, arr: list[int]) -> bool:
        # Use a set to store numbers we've seen for O(1) lookup time
        seen = set()
        
        for num in arr:
            # Check if the current number's double or half (if not zero) exists in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        
        # If we've gone through all numbers without finding a match
        return False

    checkIfExist = check_if_exist
