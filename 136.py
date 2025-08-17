class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        our_dict = {num:True for num in nums}
        for num in nums:
            our_dict[num] = not our_dict[num] # flip truth value
        for num in our_dict.keys():
            if not our_dict[num]:
                return num
        return 0
