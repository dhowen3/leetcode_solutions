import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        counts = {num:nums.count(num) for num in nums}
        unique_nums = list(counts.keys())
        unique_nums = sorted(unique_nums)
        k1 = len(unique_nums)
        d = dict() 

        # 3 unique nums
        self.unique_nums = unique_nums
        for i in range(k1):
            num1 = unique_nums[i]
            for j in range(i+1,k1):
                num2 = unique_nums[j]
                num3p = -num1 - num2
                k = bisect.bisect_left(unique_nums,num3p)
                if k < k1 and  k > j and unique_nums[k] == num3p:
                    to_return.append([num1,num2,num3p])

        # two unique_nums
        two_nums = [num for num in counts.keys() if counts[num] >= 2]
        k2 = len(two_nums) 
        for i in range(k2):
            num = two_nums[i]
            desired = -2 * num
            s_i = bisect.bisect_left(unique_nums,-2 * num)
            if num != 0 and s_i < k1 and unique_nums[s_i] == desired:
                to_return.append([num,num, -2 * num])
        if 0 in counts.keys() and counts[0] >= 3:
            to_return.append([0,0,0])
        return to_return
