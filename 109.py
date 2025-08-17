# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def helper(self, low_ptr, high_ptr):
        dif = high_ptr - low_ptr
        mid = low_ptr + dif // 2
        print(mid)
        if dif <= 0: 
            return None
        node = TreeNode(val=self.arr[mid])
        # base cases
        if dif == 1: 
            return node
        # recursive case
        node.left = self.helper(low_ptr,mid)
        node.right = self.helper(mid + 1,high_ptr)
        return node


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        while head is not None:
            self.arr.append(head.val)
            head = head.next
        n = len(self.arr)
        print("n=",n)
        return self.helper(0, n)
