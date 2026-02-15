# https://leetcode.com/problems/add-binary


class Solution:
    """67. Add Binary
    
    Given two binary strings a and b, return their sum as a binary string.
    """
    def add_binary(self, a: str, b: str) -> str:
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        # Process bits from least significant to most significant
        while i >= 0 or j >= 0 or carry:
            # Extract current bit (0 if string exhausted)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Sum current bits and carry
            total = bit_a + bit_b + carry
            
            # Current result bit is total mod 2
            result.append(str(total % 2))
            
            # Carry becomes the integer division by 2
            carry = total // 2
            
            # Move to next higher bit position
            i -= 1
            j -= 1
        
        # Result built backwards; reverse it
        result.reverse()
        
        return "".join(result)
    
    addBinary = add_binary