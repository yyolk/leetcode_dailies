# https://leetcode.com/problems/compare-version-numbers/


class Solution:
    """165. Compare Version Numbers

    Given two **version strings**, `version1` and `version2`, compare them. A version
    string consists of **revisions** separated by dots `'.'`. The **value of the
    revision** is its **integer conversion** ignoring leading zeros.

    To compare version strings, compare their revision values in **left-to-right
    order**. If one of the version strings has fewer revisions, treat the missing
    revision values as `0`.

    Return the following:

    * If `version1 < version2`, return -1.

    * If `version1 > version2`, return 1.

    * Otherwise, return 0."""

    def compare_version(self, version1: str, version2: str) -> int:
        # Split version strings into lists of revisions
        rev1 = version1.split('.')
        rev2 = version2.split('.')
        
        # Determine the maximum length to iterate up to
        max_len = max(len(rev1), len(rev2))
        
        # Iterate through each revision position
        for i in range(max_len):
            # Get revision values, default to 0 if index out of range; int() ignores leading zeros
            v1 = int(rev1[i]) if i < len(rev1) else 0
            v2 = int(rev2[i]) if i < len(rev2) else 0
            
            # Compare current revisions
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        # All revisions equal
        return 0

    compareVersion = compare_version
