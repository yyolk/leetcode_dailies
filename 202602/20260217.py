# https://leetcode.com/problems/binary-watch


class Solution:
    """401. Binary Watch
    
    A binary watch has 4 LEDs on the top to represent the hours (0-11), and
    6 LEDs on the bottom to represent the minutes (0-59). Each LED represents
    a zero or one, with the least significant bit on the right.
    
    Given an integer turnedOn which represents the number of LEDs that are
    currently on (ignoring the PM), return all possible times the watch could
    represent. You may return the answer in any order.
    
    The hour must not contain a leading zero.
    For example, "01:00" is not valid. It should be "1:00".
    The minute must consist of two digits and may contain a leading zero.
    For example, "10:2" is not valid. It should be "10:02".
    """
    def read_binary_watch(self, turned_on: int) -> list[str]:
        # Result list for valid times
        result = []
        
        # Try all valid hours (0-11)
        for hour in range(12):
            # Precompute lit LEDs for this hour
            hour_bits = bin(hour).count("1")
            
            # Try all valid minutes (0-59)
            for minute in range(60):
                # Compute lit LEDs for this minute
                minute_bits = bin(minute).count("1")
                
                # If total lit LEDs match the requirement
                if hour_bits + minute_bits == turned_on:
                    # Format time: hour as-is, minute always two digits
                    result.append(f"{hour}:{minute:02d}")
        
        return result

    readBinaryWatch = read_binary_watch