# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepthHelper(self, current: Optional[TreeNode]) -> int:
        # base case
        if current.left is None and current.right is None:
            return 1
        # recursive case
        left_height = float('inf')
        right_height = float('inf')
        if current.left is not None:
            left_height = 1 + self.minDepth(current.left)
        if current.right is not None:
            right_height = 1 + self.minDepth(current.right)
        return min(left_height, right_height)

        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        to_return = 0
        if root is not None:
            to_return = self.minDepthHelper(root)
        return to_return
        
