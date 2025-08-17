class Solution:
    def findPivot(self, nums, low, high):
        if high - low <= 1:
            return low
        middle = low + (high - low) // 2
        if nums[middle] < nums[low]:
            return self.findPivot(nums, low,middle)
        else:
            return self.findPivot(nums, middle, high)
    
    def findMin(self, nums: List[int]) -> int:
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]
        pivot = self.findPivot(nums,0, len(nums))
        if pivot < len(nums) - 1: pivot += 1
        print(pivot)
        return nums[pivot]

        
