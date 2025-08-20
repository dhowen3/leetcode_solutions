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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode sentinel = new ListNode(0, head); 
        ListNode prev = sentinel;
        ListNode distinct = head;
        while (distinct != null) {
            ListNode scout = distinct.next;
            boolean repeated = false;
            while (scout != null && scout.val == distinct.val) {
                repeated = true;
                distinct.next = scout.next;
                scout = scout.next;
            }
            if (!repeated) {
                prev = prev.next;
            } else {
                prev.next = scout;
            }
            distinct = distinct.next;
        }
        return sentinel.next;
    }
}
