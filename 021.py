# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_head = ListNode(-1, None) # temp entry for head
        current = list_head
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    current.next = list1
                    current = current.next
                    list1 = list1.next 
                else:
                    current.next = list2
                    current = current.next
                    list2 = list2.next 
            elif list1 is not None:
                current.next = list1
                list1 = None
            else: # list1 is none and list2 is not
                current.next = list2
                list2 = None
        return list_head.next # discard head of list

        
