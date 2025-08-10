# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class NodeOrder:
    node_val: int
    node: ListNode = field(compare=False)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.arr = []
        to_return_sentinel = ListNode()
        current = to_return_sentinel
        for node in lists:
            if node is not None:
                heappush(self.arr, NodeOrder(node_val=node.val, node=node))
        while len(self.arr) > 0:
            poppedNodeOrder = heappop(self.arr)
            popped = poppedNodeOrder.node
            if popped.next is not None:
                heappush(self.arr, NodeOrder(node_val=popped.next.val, node=popped.next))
            current.next = popped
            popped.next = None
            current = popped
        return to_return_sentinel.next
