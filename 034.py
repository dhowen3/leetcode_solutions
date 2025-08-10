class Solution:
    def search_below(self, low, high):
        if high - low <= 1: return low if self.nums[low] == self.target else self.n # make failure to find return n to make min work
                                                                                    # then change n to -1 later in main
        middle = low + (high - low) // 2
        if self.nums[low] == self.target: return low
        if self.nums[middle] == self.target: return min(middle, self.search_below(low,middle)) # the key line
        elif self.nums[middle] < self.target: return self.search_below(middle,high)
        else: return self.search_below(low, middle) 
    
    def search_above(self, low, high):
        if high - low <= 1: return low if self.nums[low] == self.target else - 1 
        middle = low + (high - low) // 2
        if self.nums[high-1] == self.target: return high - 1
        if self.nums[middle] == self.target: return max(middle, self.search_above(middle,high))  # the key line, mirrored
        elif self.nums[middle] < self.target: return self.search_above(middle,high)
        else: return self.search_above(low, middle) 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums

        if len(nums) == 0: return [-1,-1]

        self.target = target
        self.n = len(nums)

        min_index = self.search_below(0,self.n) 
        max_index = self.search_above(0,self.n)
        min_index = -1 if min_index == self.n else min_index

        return min_index, max_index
