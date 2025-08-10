class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: 
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        current_max = 1
        start_index = 0
        dp = [[False for j in range(n+1)] for i in range(n)]
        for k in range(n):
            dp[k][k] = True
            dp[k][k+1] = True
        for i in range(n-1, -1, -1):
            for j in range(i + 2, n + 1):
                dp[i][j] = s[i] == s[j-1] and dp[i+1][j-1]
                if j - i > current_max and dp[i][j]:
                    current_max = j - i
                    start_index = i
        return s[start_index:start_index + current_max] 
