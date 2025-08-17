#define MAX(A,B) A >= B ? A : B

typedef struct TreeNode* Node;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int maxDepthHelper(Node currentNode, int count) {
    // base case
    if (currentNode == NULL)
        return count;
    // recursive case
    ++count;
    int leftCount = maxDepthHelper(currentNode -> left, count);
    int rightCount = maxDepthHelper(currentNode -> right, count);
    return MAX(leftCount, rightCount);

}
int maxDepth(struct TreeNode* root){
    return maxDepthHelper(root, 0);
}
