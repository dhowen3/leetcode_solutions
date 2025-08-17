# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder_helper(self, current_node: Optional[TreeNode], \
            current_list : List[int]) -> List[int]:
        # base case
        if (current_node.left is None and current_node.right is None):
            current_list.append(current_node.val)
            return
        # recursive case
        if (current_node.left is not None):
            self.postorder_helper(current_node.left, current_list)
        if (current_node.right is not None):
            self.postorder_helper(current_node.right, current_list)
        current_list.append(current_node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        print("ok")
        to_return : List[int] = []
        if (root is None):
            return to_return
        self.postorder_helper(root, to_return)
        return to_return
