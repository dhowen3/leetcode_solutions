class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = nums1.copy()
        i, j = 0,0
        while True:
            if i == m and j == n:
                break
            elif i == m:
                nums1[i+j] = nums2[j]
                j += 1
            elif j == n:
                nums1[i+j] = new[i]
                i += 1
            elif new[i] <= nums2[j]:
                nums1[i+j] = new[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        
