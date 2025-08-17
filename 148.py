# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # construct array s.t. ith cell holds val and i
        l_i = []
        current = head
        i = 0
        while current is not None:
            l_i.append((current.val, i))
            i += 1
            current = current.next
        # now sort by current's val
        l_i = sorted(l_i, key=lambda x : x[0]) # O(nlogn)
        i, n , current = 0, len(l_i), head
        while i < n:
            current.val = l_i[i][0]
            i += 1
            current = current.next
        return head 

        
