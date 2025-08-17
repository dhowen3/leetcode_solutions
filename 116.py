"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect_helper(self, left_child, right_child):
        left_child.next = right_child
        if left_child.right is None: # since perfect, only check once
            return
        self.connect_helper(left_child.left,left_child.right)
        self.connect_helper(right_child.left,right_child.right)
        self.connect_helper(left_child.right,right_child.left)


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # root's next is none by default
        if root is None or root.left is None: return root
        self.connect_helper(root.left,root.right)
        return root
