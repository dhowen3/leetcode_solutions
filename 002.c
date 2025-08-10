typedef struct ListNode* NodePtr;

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int carry = 0;

    NodePtr newHead = malloc(sizeof(struct ListNode));
    NodePtr newTail = newHead;

    while(1) {
        int currentDigit = 0;
        currentDigit += carry;
        if (l1 == NULL && l2 == NULL) {
            break;
        }
        if (l1 != NULL) {
            currentDigit += l1 -> val;
            l1 = l1 -> next;
        }
        if (l2 != NULL) {
            currentDigit += l2 -> val;
            l2 = l2 -> next;
        }
        if (currentDigit >= 10) {
            currentDigit -= 10;
            carry = 1;
        } else {
            carry = 0;
        }
        newTail -> val = currentDigit;
        NodePtr newNode = malloc(sizeof(struct ListNode));
        newTail -> next = newNode;
        newTail = newNode;
    }
    if (carry == 1) {
        newTail -> val = 1;
        newTail -> next = NULL;
    } else {
        NodePtr currentNode = newHead;
        while (currentNode -> next != newTail) {
            currentNode = currentNode -> next;
        }
        currentNode -> next = NULL;
    }
    return newHead;
}
