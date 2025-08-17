class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        dp.append(0)
        dp.append(0)
        for index, value in enumerate(nums):
            dp_current = max(dp[-1], dp[-2] + value)
            dp.append(dp_current)
        return dp[-1]
        
