# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_helper(self, current, to_return):
        # base case
        if current is None:
            return
        self.inorder_helper(current.left, to_return)
        to_return.append(current.val)
        self.inorder_helper(current.right, to_return)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        to_return = []
        self.inorder_helper(root, to_return)
        return to_return
