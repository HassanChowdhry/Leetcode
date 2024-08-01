// https://leetcode.com/problems/binary-tree-inorder-traversal

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
 * @return {number[]}
 */

function helper(root, stack) {
  if (!root) {
    return stack;
  }
  helper(root.left, stack);
  stack.push(root.val);
  return helper(root.right, stack);
}
function inorderTraversal(root) {
  return helper(root, []);
}
