# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        sentinel_head = ListNode()
        sentinel_head.next = head
        current = sentinel_head
        for i in range(left - 1):
            current = current.next
        left_prev = current
        print(left_prev.val)
        l = []
        current = current.next
        for i in range(right - left + 1):
            l.append(current)
            current = current.next
        right_next = current
        for i in range(len(l) - 1, 0, -1):
            l[i].next = l[i-1]
        left_prev.next = l[-1]
        l[0].next = right_next
        del l
        return sentinel_head.next
