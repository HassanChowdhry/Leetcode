// https://leetcode.com/problems/range-sum-of-bst

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
function helper(currentRoot, low, high, sum) {
  if (!currentRoot) {
    return sum;
  }
  if (currentRoot.val >= low && currentRoot.val <= high) {
    sum += currentRoot.val;
  }
  return sum + helper(currentRoot.left, low, high, 0) + helper(currentRoot.right, low, high, 0); 
}

function rangeSumBST(root, low, high) {
  return helper(root, low, high, 0);
}
