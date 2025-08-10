/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode* NodePtr;
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    NodePtr leadNode = head;
    NodePtr followNode = head;
    int leadToFollowDistance = 0;
    while (leadNode != NULL) {
        leadNode = leadNode -> next;
        if (leadToFollowDistance < n + 1) {
            ++leadToFollowDistance;
        } else {
            followNode = followNode -> next;
        }
    }
    // printf("n : %d, followNode : %d\n", n, followNode -> val);
    if (leadToFollowDistance == n) {
        return head -> next;
    }
    NodePtr toDelete = followNode -> next;
    if (toDelete -> next == NULL) {
        followNode -> next = NULL;
    } else {
        NodePtr toAttach = toDelete -> next;
        followNode -> next = toAttach;
    }
    return head;

}
