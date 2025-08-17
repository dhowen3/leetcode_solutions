# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        current = head
        # add to queue
        while current is not None:
            q.append(current)
            current = current.next
        current = q.popleft() # head
        right = True
        # pop from queue, alternating right and left
        while len(q) > 0:
            popped = q.pop() if right else q.popleft()
            current.next = popped
            right = not right
            current = popped
        current.next = None
        return head
