class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        index = -1
        num_digits = len(digits)

        while(carry and index >= -num_digits):
            if digits[index] != 9:
                digits[index] += 1
                carry = False
            else: # current digit is 9
                digits[index] = 0
            index -= 1

        if carry and index == -num_digits - 1:
            digits.insert(0,1)

        return digits

        
