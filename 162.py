from random import randint

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        # one elt case
        if n == 1: return 0
        # check ends of array
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return n - 1
        # random algorithm now
        while True:
            index = randint(1,n-1)
            if nums[index] > nums[index-1] and nums[index] > nums[index+1]:
                return index
        return -1

