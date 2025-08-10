class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m,n
        to_return = ""
        carry = False
        while True:
            i, j = i - 1, j -1
            if i < 0 and j < 0 and not carry:
                break
            if i < 0 and j < 0 and carry:
                to_return = '1' + to_return
                break
            current_a = int(a[i]) if i >= 0 else 0
            current_b = int(b[j]) if j >= 0 else 0
            current_c = 1 if carry else 0
            match current_a + current_b + current_c:
                case 0:
                    to_return = "0" + to_return
                    carry = False
                case 1: 
                    to_return = "1" + to_return
                    carry = False
                case 2: 
                    to_return = "0" + to_return
                    carry = True
                case 3:
                    to_return = "1" + to_return
                    carry = True
                
        return to_return
