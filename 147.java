/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    // given a -> b and inserting c, results in a -> b -> c
    public void insertNode(ListNode toInsert, ListNode prevNode) {
        // System.out.println("inserting " + toInsert.val + " after " + prevNode.val + " and before " )
        ListNode temp = prevNode.next;
        prevNode.next = toInsert;
        toInsert.next = temp;
    }

    public void insertIntoList(ListNode sentinel, ListNode toInsert) {
        ListNode current;
        boolean inserted = false;
        for (current = sentinel; current.next != null; current = current.next) {
            if (toInsert.val <= current.next.val) {
                inserted = true;
                insertNode(toInsert, current);
                break;
            }
        }
        if (!inserted) {
            assert(current.next == null);
            current.next = toInsert;
            toInsert.next = null;
        }
    }

    public ListNode insertionSortList(ListNode head) {
        ListNode sentinel = new ListNode();
        sentinel.next = head;
        if (head.next == null) {
            return head;
        }
        ListNode iterator = head.next;
        ListNode iteratorNext;
        head.next = null; // split into left and right
                          // left - sorted list & right - iterator
        while (iterator != null) {
            ListNode toCompare = sentinel;
            iteratorNext = iterator.next;
            iterator.next = null; // split
            insertIntoList(sentinel, iterator);
            iterator = iteratorNext;
        }
        return sentinel.next;
    }
    
}
