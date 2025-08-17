/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        for (ListNode currentA = headA; currentA != null; currentA = currentA.next) {
            for (ListNode currentB = headB; currentB != null; currentB = currentB.next) {
                if (currentA == currentB) {
                    return currentA;
                }
            }
        }
        return null;
    }
}
