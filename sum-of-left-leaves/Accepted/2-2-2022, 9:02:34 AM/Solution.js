// https://leetcode.com/problems/sum-of-left-leaves

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
 * @return {number}
 */
var sumOfLeftLeaves = function(root) {
     if (!root) {
    return 0;
  }

  if (root.left && (!root.left.left && !root.left.right)) {
    return root.left.val + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
  }

  return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
};