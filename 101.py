# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_symmetric_helper(self, ptr1, ptr2):
        # base case 1:
        if ptr1 is None and ptr2 is None:
            return True 
        # base case 2:
        if ((ptr1 is None) ^ (ptr2 is None) == 1) or (ptr1.val != ptr2.val):
            return False
        # recursive case
        return self.is_symmetric_helper(ptr1.left, ptr2.right) and self.is_symmetric_helper(ptr1.right, ptr2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.is_symmetric_helper(root.left, root.right)

        
