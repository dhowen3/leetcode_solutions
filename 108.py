# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def arr_to_bst_helper(self, low, high):
        if high == low: return None
        middle = low + (high - low) // 2
        current = TreeNode(self.nums[middle])
        current.left = self.arr_to_bst_helper(low, middle)
        current.right = self.arr_to_bst_helper(middle+1,high)
        return current

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.arr_to_bst_helper(0,len(nums))
