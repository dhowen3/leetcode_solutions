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

 // i looked at this one in summer 2024 and couldn't crack it and 
 // came back and cracked it summer 2025! great success!
class Solution {
    public Solution(){
        this.splits = new LinkedList();
        this.dp = new LinkedList();
    }

    // each row in splits holds - given n - ways in which two ints x + y = n
    // example : n = 3
    // splits holds : {[0,3], [1,2], [2,1], [3,0]}

    public LinkedList<LinkedList<Integer[]>> splits;

    // ith row in dp holds all possible binary trees with i nodes
    // note nodes in each tree are unlabelled until after nth row is filled in
    public LinkedList<LinkedList<TreeNode>> dp;

    // make aforementioned splits array
    public void makeSplits(int n) {
        for (int i = 0; i <= n; ++i) {
            LinkedList<Integer[]> newRow = new LinkedList<Integer[]>();
            for (int j = 0; j <= i; ++j) {
                newRow.add(new Integer[]{j,i-j});
            }
            this.splits.add(newRow);
        }
    }

    // clone a tree given a tree to clone and a node for the new tree's cloned head.
    // if cloned head is null , immediately return
    public void cloneTree(TreeNode current, TreeNode copyCurrent) {
        if (copyCurrent == null) {
            return;
        }
        if (current.left != null) {
            TreeNode copyLeft = new TreeNode();
            copyCurrent.left = copyLeft;
            cloneTree(current.left, copyLeft);
        }
        if (current.right != null) {
            TreeNode copyRight = new TreeNode();
            copyCurrent.right = copyRight;
            cloneTree(current.right, copyRight);
        }
    }

    // given a head of a tree with n nodes, currently unlabelled,
    // assign vals to each of the tree's nodes
    // following normal b.s.t. rules
    // use an in-order traversal to accomplish this.
    public int relabelTree(TreeNode current, int currentVal) {
        if (current == null) {
            return currentVal;
        }
        currentVal = relabelTree(current.left, currentVal);
        current.val = currentVal;
        return relabelTree(current.right, currentVal + 1);
    }

    // the observation is that we given that all trees with < n nodes are defined in dp,
    // we are able to simply assign each of those to the left and right child of a 
    // newly created head node , based on previously defined splits
    // in this way, dp is built row by row
    //
    // example : n = 3.
    // then define a head node at each iteration, 
    // 1st iteration, split = (0,2): left child of head left null, right child assigned all trees of size 2
    // 2nd iteration, split = (1,1): left child and right child both assigned all trees of size 1 (single node)
    // 3rd iteration, split = (2,0): reverse of 1st iteration
    //
    public void genTreesHelper(int nodesRemaining, List<TreeNode> returnList) {
        List<Integer[]> currentSplit = this.splits.get(nodesRemaining - 1);  
        for (Integer[] split: currentSplit) {
            for (TreeNode leftTree: dp.get(split[0])) {
                for (TreeNode rightTree: dp.get(split[1])) {
                    TreeNode newHead = new TreeNode();
                    TreeNode leftHead = split[0] == 0 ? null : new TreeNode();
                    cloneTree(leftTree, leftHead);
                    TreeNode rightHead = split[1] == 0 ? null : new TreeNode();
                    cloneTree(rightTree, rightHead);
                    newHead.left = leftHead;
                    newHead.right = rightHead;
                    returnList.add(newHead);
                }
            }
        }
    }

    public List<TreeNode> generateTrees(int n) {
        makeSplits(n);
        // 0th row - empty list
       LinkedList<TreeNode> dpZerothRow = new LinkedList<TreeNode>();
        dpZerothRow.add(null);
        dp.add(dpZerothRow);
        // 1st row - one node
        LinkedList<TreeNode> dpFirstRow = new LinkedList<TreeNode>();
        dpFirstRow.add(new TreeNode());
        dp.add(dpFirstRow);
        for (int i = 2; i<=n; ++i) {
            LinkedList<TreeNode> dpRow = new LinkedList();
            genTreesHelper(i, dpRow);
            this.dp.add(dpRow);
        }
        LinkedList<TreeNode> toReturn = dp.get(n);
        for (TreeNode head : toReturn) {
            relabelTree(head, 1);
        }
        return toReturn;
    }
} 
