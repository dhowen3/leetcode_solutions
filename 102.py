# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        to_return = []
        queue = deque()
        if root is not None:
            queue.append((root, 0))
        while len(queue) > 0:
            current_tuple = queue.popleft()
            current_node = current_tuple[0]
            i = current_tuple[1]
            for child_node in (current_node.left, current_node.right):
                if child_node is not None:
                    queue.append((child_node, i + 1))
            while len(to_return) < i + 1:
                to_return.append([])
            to_return[i].append(current_node.val)
        return to_return
