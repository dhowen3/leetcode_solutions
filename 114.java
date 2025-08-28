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
    public void rotateRight(TreeNode current, TreeNode precursor) {
        if (precursor == null) {
            return;
        }
        TreeNode tempRight = current.right;
        current.right = current.left;
        current.left = null;
        precursor.right = tempRight;
    }

    public TreeNode flattenHelper(TreeNode root) { // return precursor
        TreeNode precursor = null;
        // base case :
        if (root.left == null && root.right == null) {
            return root;
        } else if  (root.left != null && root.right == null) {
            precursor = flattenHelper(root.left);
            rotateRight(root, precursor);
            return precursor;
        } else if (root.left == null && root.right != null) {
            precursor = flattenHelper(root.right);
            return precursor;
        } else { // (root.left != null && root.right != null)
            precursor = flattenHelper(root.left);
            TreeNode newPrecursor = flattenHelper(root.right);
            rotateRight(root, precursor);
            return newPrecursor;
        }
    }

    public void flatten(TreeNode root) {
        if (root != null) {
            flattenHelper(root);
        }
    }
}
