class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0 
        num_dups = 0
        n = len(nums)
        current_max = nums[0] - 1
        while ptr1 < n and ptr2 < n:
            while nums[ptr2] <= current_max:
                if ptr2 + 1 < n:
                    num_dups += 1
                    ptr2 += 1
                else:
                    break
            current_max = nums[ptr2]
            nums[ptr1] = nums[ptr2]
            ptr1 += 1
        # lazy ! 
        the_count = 0
        current_max = nums[0] - 1
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
                the_count += 1
            else:
                break
        return the_count
