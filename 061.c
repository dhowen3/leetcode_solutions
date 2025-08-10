typedef struct ListNode* Node;

Node getNode(Node head, int index) {
    Node currentNode = head;
    for (int i = 0; i < index; ++i) {
        currentNode = currentNode -> next;
    }
    return currentNode;
}

int getListSize(Node head) {
    int count = 0;
    Node currentNode = head;
    while (currentNode != NULL) {
        ++count;
        currentNode = currentNode -> next;
    }
    return count;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k){
    int listSize = getListSize(head); 
    if (listSize <= 1) {
        return head;
    }
    k %= listSize;
    if (k == 0) {
        return head;
    }
    Node newTail = getNode(head, listSize - k - 1);
    Node newHead = getNode(head, listSize - k);
    Node oldTail = getNode(head, listSize - 1);
    oldTail -> next = head;
    newTail -> next = NULL; 
    return newHead;
}
