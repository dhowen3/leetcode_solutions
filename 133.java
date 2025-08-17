/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

// approach : 
// step 1:
// create hashmap of vals {1..100} mapping to cloned Nodes
// step 2:
// create adjacency matrix {1..100} from given original graph
// step 3:
// using created hashmap and adjacency matrix, mark cloned nodes as neighbors

class Solution {
    // edits the nodes (their neighbors specifically) in the hashmap passed as first argument
    public void constructClonedFromAdjMatrix(HashMap<Integer, Node> clonedNodeMap, boolean[][] adjMatrix) {
        // note in loops we should only be accessing each (i,j) pair once which eliminates the need to
        // check if such-and-such already has so-and-so as a neighbor
        for (int i = 0; i < 100; ++i) {
            for (int j = 0; j < i; ++j) {
                if (adjMatrix[i][j]) {
                    clonedNodeMap.get(i + 1).neighbors.add(clonedNodeMap.get(j + 1));
                    clonedNodeMap.get(j + 1).neighbors.add(clonedNodeMap.get(i + 1));
                }
            }
        }
    }

    public void fillAdjMatrixWithBFS(Node startNode, boolean[][] adjMatrix) {
        boolean[] visited = new boolean[100];
        LinkedList<Node> bfsQueue = new LinkedList<Node>();
        bfsQueue.add(startNode);
        while (!bfsQueue.isEmpty()) {
            Node currentNode = bfsQueue.pop();
            int i = currentNode.val - 1;
            if (visited[i]) {
                continue;
            } else {
                visited[i] = true;
            }
            for (Node neighbor : currentNode.neighbors) {
                int j = neighbor.val - 1;
                adjMatrix[i][j] = true;
                adjMatrix[j][i] = true;
                if (!visited[j]) {
                    bfsQueue.add(neighbor);
                }
            }

        }
        System.out.println("step");
    }

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        int startNodeVal = node.val;

        HashMap<Integer, Node> clonedNodeMap = new HashMap<Integer, Node>();
        for (int i = 1; i <= 100; ++i) {
            clonedNodeMap.put(i, new Node(i));
        }

        boolean[][] adjMatrix = new boolean[100][100]; // remember to increment by 1 when accessing row, col

        constructClonedFromAdjMatrix(clonedNodeMap, adjMatrix);
        fillAdjMatrixWithBFS(node, adjMatrix);
        constructClonedFromAdjMatrix(clonedNodeMap, adjMatrix);

        return clonedNodeMap.get(startNodeVal);
    }
}
