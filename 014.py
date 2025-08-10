class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count : int = 0
        for j in range(len(strs[0])):
            current_char : chr = strs[0][j]
            for i in range(1, len(strs)):
                if len(strs[i]) <= j:
                    return strs[0][:count]
                if strs[i][j] != current_char:
                    return strs[0][:count]
            count += 1
        return strs[0][:count]
