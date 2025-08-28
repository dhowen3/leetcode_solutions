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


 // in order - left current right.


 // push nodes onto 2 stacks.

class BSTIterator {
    public LinkedList<TreeNode> stack;
    public LinkedList<TreeNode> stack2;

    public BSTIterator(TreeNode root) {
        this.stack = new LinkedList<TreeNode>(); // nodes that haven't yet been recursed left
        this.stack2 = new LinkedList<TreeNode>(); // nodes that have already been recursed left
        this.stack.push(root);
    }
    
    public int next() {
        while (!this.stack.isEmpty() && this.stack.peekFirst().left != null) {
            TreeNode popped = this.stack.pop();
            this.stack2.push(popped);
            this.stack.push(popped.left);
        }
        TreeNode current = this.stack.isEmpty() ? this.stack2.pop() : this.stack.pop();
        if (current.right != null) {
            stack.push(current.right);
        }
        return current.val;

    }
    
    public boolean hasNext() {
        return !(this.stack.isEmpty() && this.stack2.isEmpty());
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
