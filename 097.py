class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # confirm lengths ok
        if len(s1) + len(s2) != len(s3):
            return False
        #s1 across the column, s2 across the rows
        dp = [[False for j in range(len(s1)+1)] for i in range(len(s2)+1)]
        # populate first row
        for j in range(len(s1)+1):
            if s1[:j] == s3[:j]:
                dp[0][j] = True
            else: 
                break
        # populate first col
        for i in range(len(s2)+1):
            if s2[:i] == s3[:i]:
                dp[i][0] = True
            else: 
                break
        # populate the rest
        for i in range(1,len(s2)+1):
            for j in range(1,len(s1)+1):
                if dp[i-1][j] and s3[i+j-1] == s2[i-1]:
                    dp[i][j] = True
                elif dp[i][j-1] and s3[i+j-1] == s1[j-1]:
                    dp[i][j] = True
        return dp[len(s2)][len(s1)]
