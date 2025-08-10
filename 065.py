class Solution:
    def isNumber(self, s: str) -> bool:
        # check 1 - no invalid chars
        s = s.lower()
        digits = [chr(i) for i in range(ord('0'), ord('9') + 1)] 
        other = ['e','+','-','.']
        allowed = digits + other
        for char in s:
            if char not in allowed: return False
        # split by exponent
        spl = s.split('e')
        if len(spl) >= 3: return False
        after_exponent = False
        # analyze each
        for spl_i in spl:
            if (spl_i_len := len(spl_i)) == 0: return False
            print(spl_i_len)
            period_count = spl_i.count('.')
            plus_count = spl_i.count('+')
            minus_count = spl_i.count('-')
            if plus_count + minus_count >= 2: return False
            elif plus_count + minus_count == 1:
                if len(spl_i) <= 1 or (spl_i[0] != '-' and spl_i[0] != '+'): return False
            if period_count >= 2: return False
            elif period_count == 1 and (spl_i_len - plus_count - minus_count <= 1): return False
            elif period_count == 1 and after_exponent: return False 
            after_exponent = True
        return True
