class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1 for i in range(n)]
        dp[-1] = 0 # "base case"
        print(n)
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                dp[i] = n + 1 # value for "infinity"
                continue
            min_jump_range = i + 1
            max_jump_range = min(min_jump_range+nums[i],n)
            dp[i] = 1 + min(dp[min_jump_range:max_jump_range])
        return dp[0]
            
