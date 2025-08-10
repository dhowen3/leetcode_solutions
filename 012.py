class Solution:
    def __init__(self):
        self.int_to_numeral = {1:'I', 5:'V', 10:'X',50:'L', 100:'C', 500: 'D', 1000:'M'}

    def intToRoman(self, num: int) -> str:
        num_reverse_as_str = str(num)[::-1]
        to_return = ""
        for i, digit_char in enumerate(num_reverse_as_str):
            digit = int(digit_char)
            tens_power = 10**i
            if digit == 0:
                continue
            if digit == 9:
                to_return = self.int_to_numeral[tens_power * 10] + to_return
                to_return = self.int_to_numeral[tens_power] + to_return
            elif digit == 4:
                to_return = self.int_to_numeral[tens_power * 5] + to_return
                to_return = self.int_to_numeral[tens_power] + to_return
            elif digit in range(5,9): # 5 <= digit <= 8
                digit -= 5
                to_return = (digit * str(self.int_to_numeral[tens_power])) + to_return
                to_return = self.int_to_numeral[tens_power * 5] + to_return
            else: # 1 <= digit <= 3
                to_return = (digit * str(self.int_to_numeral[tens_power])) + to_return
        return to_return
