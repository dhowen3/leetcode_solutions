# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_balanced_helper(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self.is_balanced_helper(current_node.left, current_height + 1)
        right_height = self.is_balanced_helper(current_node.right, current_height + 1)
        if abs(right_height - left_height) > 1:
            return -1
        else:
            return max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balanced_helper(root, 0) != -1
        
