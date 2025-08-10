# grade-school multiplication algo. there is better runtime div-and-conquer
# method that exists.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        to_return_num = 0
        m, n = len(num1), len(num2)
        for i in range(m-1,-1,-1):
            multiplier = 10**(m - 1 - i)
            digit1 = int(num1[i])
            for j in range(n-1,-1,-1):
                digit2 = int(num2[j])
                to_return_num += multiplier * digit1 * digit2
                multiplier *= 10
        return str(to_return_num)
