class Solution:
    def __init__(self):
        self.max_profit = 0

    def merge_sort(self,nums):
        n = len(nums)
        if n == 1:
            return nums
        middle = n // 2
        left = self.merge_sort(nums[:middle])
        right = self.merge_sort(nums[middle:])
        self.max_profit = max(self.max_profit, right[-1] - left[0])
        return self.merge(left,right)

    def merge(self,nums1, nums2):
        x = len(nums1)
        y = len(nums2)
        i = 0
        j = 0
        r = []
        while True:
            if i == x and j == y:
                return r
            elif i == x:
                r.append(nums2[j])
                j += 1
            elif j == y:
                r.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1

    # reduce to merge sort
    def maxProfit(self, prices: List[int]) -> int:
        self.merge_sort(prices)
        return self.max_profit
