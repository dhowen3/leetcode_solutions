# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_numbers_helper(self, current, current_num):
        current_num = int(str(current_num)+ str(current.val))
        # base case - leaf node
        if current.left is None and current.right is None:
            return current_num
        # recursive case
        if current.left is not None and current.right is not None:
            return self.sum_numbers_helper(current.left, current_num) + self.sum_numbers_helper(current.right, current_num)
        elif current.left is not None:
            return self.sum_numbers_helper(current.left, current_num)
        else:
            return self.sum_numbers_helper(current.right, current_num)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum_numbers_helper(root, "")
        
