// tortoise and the hare algorithm
// pretty slick. should stay in long-term memory

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
    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }
        ListNode ptr1 = head;
        ListNode ptr2 = head;
        boolean started = false;
        while (!ptr1.equals(ptr2) || !started) {
            started = true;
            if (ptr2.next == null || ptr2.next.next == null) {
                return false;
            }
            ptr1 = ptr1.next; // ptr1 moves one at a time
            ptr2 = ptr2.next.next; // ptr2 moves two at a time.
            /*
            System.out.println(ptr1.val);
            System.out.println(ptr2.val);
            System.out.println();
            */
        }
        // if we want to return which node is the cycle start,
        // upon exiting loop reset ptr2 to head and move one-node-at-a-time now  
        // until they equal each other
        return true;
    }
}
