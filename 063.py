class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # make useful assignments
        m = len(obstacleGrid) 
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        # set cell at 0,0 in dp to 1 if no obstacle there else return 0
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        # set 1st col
        print("new testcase")
        print(dp)
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        # set 1st row
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        # set rest of dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    pass
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return
        return dp[m-1][n-1]
