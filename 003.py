from string import printable, whitespace

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c,m,i,j,n = 0,0,-1,0,len(s) # c - current count, # m - max count, i - window low index, j - window high index, n - len of s
        chars = {char:(False, -1) for char in printable + whitespace}
        while j < n:
            if chars[s[j]][0]:
                i = max(i, chars[s[j]][1])
            chars[s[j]] = (True, j)
            c = j - i
            m = max(m, c)
            j += 1
        return m
