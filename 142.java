// tortoise & hare

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode ptr1 = head, ptr2 = head;
        boolean started = false;
        while (!ptr1.equals(ptr2) || !started) {
            started = true;
            if (ptr2.next == null || ptr2.next.next == null) {
                return null;
            }
            ptr1 = ptr1.next;
            ptr2 = ptr2.next.next;
        }
        ptr2 = head;
        while (!ptr1.equals(ptr2)) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }
        return ptr1;
        
    }
}
