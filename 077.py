class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        to_return = []
        for i in range(2**n):
            mapping = r""+str(bin(i))[2:]
            if mapping.count('1') != k: continue
            mapping = (n-len(mapping)) * '0' + mapping
            current = []
            for i in range(n): 
                if mapping[i] == '1': 
                    current.append(i+1)
            to_return.append(current)
        return to_return
