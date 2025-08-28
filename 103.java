/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // this can be classified as a lazy first-idea solution
    // and there is a slicker way to do this surely. 
    // 

    public void makeOneDList(TreeNode currentNode, int currentHeight, List<Integer[]> oneDList) {
        System.out.println(currentNode.val + " " + currentHeight);
        oneDList.add(new Integer[]{currentNode.val, currentHeight});
        if (currentNode.left != null) {
            makeOneDList(currentNode.left, currentHeight + 1, oneDList);
        }
        if (currentNode.right != null) {
            makeOneDList(currentNode.right, currentHeight + 1, oneDList);
        }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return new LinkedList<List<Integer>>();
        }
        // create 1-d array of 2-tuples - value and height. pre-order traversal
        LinkedList<Integer[]> oneDList = new LinkedList<Integer[]>();
        makeOneDList(root, 0, oneDList);
        int currentHeight = 0;
        List<List<Integer>> toReturn = new LinkedList<List<Integer>>();
        LinkedList<Integer> currentRow = new LinkedList<Integer>();

        for (Integer[] entry : oneDList) {
            if (entry[1] > currentHeight) {
                toReturn.add(currentRow);
                currentRow = new LinkedList<Integer>();
                currentHeight = entry[1];
            }
            if (entry[1] == currentHeight && entry[1] % 2 == 0) { // even row
                currentRow.add(entry[0]);
            } else if (entry[1] == currentHeight) {
                currentRow.push(entry[0]);
            } else if (entry[1] % 2 == 0) {
                toReturn.get(entry[1]).add(entry[0]);
            } else {
                toReturn.get(entry[1]).add(0, entry[0]);
            }
        }
        toReturn.add(currentRow);
        return toReturn;
    }
}
