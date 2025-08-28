class Solution {

    class Node {
        public Node(int startIndex) {
            this.gasRemaining = 0;
            this.next = null;
            this.startIndex = startIndex;
        }
        int gasRemaining;
        Node next;
        int startIndex;
    }

    public Node makeCircularLL(int[] net) {
        Node sentinel = new Node(1);
        Node current = sentinel;
        int i = 0, n = net.length;

        while (i < n) {

            int j = i + 1;
            int sum = net[i];

            while (j < n && sum >= 0 && sum + net[j] >= 0) { 
                sum += net[j];
                ++j;
            }

            Node newNode = new Node(i);
            newNode.gasRemaining = sum;
            current.next = newNode;
            current = newNode;
            i = j; 
        }

        current.next = sentinel.next;  // making it circular
        return sentinel.next;
    }



    public int[] makeNet(int[] gas, int[] cost) {
        int[] toReturn = new int[gas.length];
        for (int i = 0; i < gas.length; ++i) {
            toReturn[i] = gas[i] - cost[i];
        }
        return toReturn;
    }

/*
    outer loop - forcibly increment next
    inner loop - increment conditionally if gas remaining at termination >= running gas total
    if inner loop loops back to its starting node return true
    if outer loop loops back to its starting node return false
*/
    public int containsValidCircuit(Node head) {
        if (head.next == head) { // one node in list, self-loop
            return head.gasRemaining >= 0 ? head.startIndex : -1;
        }

        Node outerCurrent = head;
        do {
            int gasSum = outerCurrent.gasRemaining;
            Node innerCurrent = outerCurrent.next; 
            System.out.println("outer current index: " + outerCurrent.startIndex);
            System.out.println();
            while (outerCurrent != innerCurrent && gasSum >= 0 && gasSum + innerCurrent.gasRemaining >= 0) {
                gasSum += innerCurrent.gasRemaining;
                innerCurrent = innerCurrent.next;
                System.out.println("outer current index: " + outerCurrent.startIndex);
                System.out.println("inner current index: " + innerCurrent.startIndex);
                System.out.println("gas sum: " + gasSum);
                System.out.println();
            }
            if (outerCurrent == innerCurrent) {
                return outerCurrent.startIndex;
            } else {
                outerCurrent = outerCurrent.next;
            }
        } while (outerCurrent != head);
        return -1;
    }
    


    public int canCompleteCircuit(int[] gas, int[] cost) {
        int[] net = makeNet(gas, cost);
        Node llHead = makeCircularLL(net);
        Node current = llHead;
        System.out.println("list info:");
        do {
            System.out.println(current.startIndex);
            System.out.println(current.gasRemaining);
            System.out.println();
            current = current.next;
        } while (current != llHead);
        System.out.println();
        return containsValidCircuit(llHead);
    }
}
