class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        upper_bound = (10**5) + 1 
        z_plus = [False for i in range(upper_bound)]
        for num in nums:
            if num >=1 and num < upper_bound:
                z_plus[num-1] = True
        min_num = -1
        for i in range(upper_bound):
            if not z_plus[i]:
                min_num = i + 1
                break
        return min_num

