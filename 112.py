# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def has_path_sum_helper(self, current_node : Optional[TreeNode], target_sum : int, \
                            current_sum: int) -> bool:
        current_sum += current_node.val
        # base case
        if current_node.left is None and current_node.right is None:
            return current_sum == target_sum
        # recursive case
        left_path_sum : bool = False
        if current_node.left is not None:
            left_path_sum  = self.has_path_sum_helper(current_node.left, target_sum, current_sum)
        right_path_sum : bool = False
        if current_node.right is not None:
            right_path_sum  = self.has_path_sum_helper(current_node.right, target_sum, current_sum)
        return left_path_sum or right_path_sum


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.has_path_sum_helper(root, targetSum, 0)

