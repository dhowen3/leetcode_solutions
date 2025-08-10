class Solution:
    def make_arr(self, input_str):
        to_return = [0 for i in range(26)]
        for char in input_str:
            to_return[ord(char) - ord('a')] += 1
        return to_return

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        arrs = [self.make_arr(s) for s in strs]
        match_found = [False for i in range(n)]
        to_return = []
        for i, arr in enumerate(arrs):
            current = []
            current.append(strs[i])
            if match_found[i]:
                continue
            for j in range(i+1, n):
                if arrs[i] == arrs[j]:
                    current.append(strs[j]) 
                    match_found[j] = True
            to_return.append(current)
        return to_return
            
            
