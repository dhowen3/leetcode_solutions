/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> map = new HashMap<Node, Node>();

        Node copyHead = head == null ? null : new Node(-1);
        Node origCurrent = head;
        Node copyCurrent = copyHead;

        while (origCurrent != null) {
            Node copyNext = origCurrent.next == null ? null : new Node(-1);
            map.put(origCurrent, copyCurrent);
            copyCurrent.val = origCurrent.val;
            copyCurrent.random = origCurrent.random;
            origCurrent = origCurrent.next;
            copyCurrent.next = copyNext;
            copyCurrent = copyNext;
        }
        copyCurrent = copyHead;
        while (copyCurrent != null) {
            copyCurrent.random = map.get(copyCurrent.random);
            copyCurrent = copyCurrent.next;
        }
        return copyHead;
    }
}
