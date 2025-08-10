# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        current = head
        prev = new_head
        while current is not None and current.next is not None:
            down_one = current.next
            down_two = down_one.next
            prev.next = down_one
            down_one.next = current
            current.next = down_two
            prev = current
            current = down_two
        return new_head.next
