# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.to_return = []
        self.target_val = 0

    def helper(self, current_node, current_list):
        current_list.append(current_node.val)
        # base case - leaf node
        if current_node.left is None and current_node.right is None:
            if sum(current_list) == self.target_val:
                self.to_return.append(current_list)
            return
        # recursive case(s)
        if current_node.left is not None:
            self.helper(current_node.left, current_list.copy())
        if current_node.right is not None:
            self.helper(current_node.right, current_list)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.target_val = targetSum
        self.helper(root, [])
        return self.to_return
