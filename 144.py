# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder_traversal_helper(self, current, to_return):
        to_return.append(current.val)
        if current.left is not None:
            self.preorder_traversal_helper(current.left, to_return)
        if current.right is not None:
            self.preorder_traversal_helper(current.right, to_return)
        return to_return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        to_return = []
        if root is not None:
            to_return = self.preorder_traversal_helper(root, [])
        return to_return
        
