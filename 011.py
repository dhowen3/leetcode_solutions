class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ptr1 = 0
        ptr2 = n - 1
        max_water = 0
        while ptr1 < ptr2:
            max_water = max(max_water, (ptr2-ptr1) * min(height[ptr2], height[ptr1]))
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return max_water
