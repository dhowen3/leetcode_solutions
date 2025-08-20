# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_ptr = head
        second_ptr = first_ptr
        while first_ptr is not None:
            current_val = first_ptr.val
            while second_ptr is not None and second_ptr.val == current_val:
                second_ptr = second_ptr.next
            first_ptr.next = second_ptr
            first_ptr = first_ptr.next
        return head
        
        
