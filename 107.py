# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_level_order(self, current_node, level):
        if current_node is None: 
            return
        if level not in self.d.keys():
            self.d[level] = []
        self.d[level].append(current_node.val)
        self.get_level_order(current_node.left, level+1)
        self.get_level_order(current_node.right, level+1)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = {}
        self.get_level_order(root,0)
        l = []
        n = len(self.d.keys())
        for i in range(n-1,-1,-1):
            l.append(self.d[i])
        return l
