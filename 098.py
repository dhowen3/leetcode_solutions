# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_valid_bst_helper(self, current, current_min, current_max):
        # base case
        if current is None:
            return True
        # recursive case
        if current_max is not None and current.val >= current_max:
            return False
        elif current_min is not None and current.val <= current_min:
            return False
        else:
            left_valid = self.is_valid_bst_helper(current.left, current_min, current.val)
            right_valid = self.is_valid_bst_helper(current.right, current.val, current_max)
            return left_valid and right_valid
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst_helper(root, None, None)
