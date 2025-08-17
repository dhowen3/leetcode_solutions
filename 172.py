from math import floor

class Solution:
    def trailingZeroes(self, n: int) -> int:
        max_power_5 = 5
        to_return = 0
        current = int(floor(n/max_power_5)) 
        while current > 0:
            to_return += current
            max_power_5 *= 5
            current = int(floor(n/max_power_5)) 
        return to_return


        
