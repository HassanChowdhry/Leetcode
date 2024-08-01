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
function rangeSumBST(root, low, high) {
  let sum = 0;
  if (!root) {
    return sum;
  }
  if (root.val >= low && root.val <= high) {
    sum += root.val;
  }
  return sum + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
}
