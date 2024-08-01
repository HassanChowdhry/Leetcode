// https://leetcode.com/problems/univalued-binary-tree

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
 * @return {boolean}
 */
function dfs(root, value) {
  if (!root) {
    return true;
  }
  if (root.val !== value) {
    return false;
  } 
  return dfs(root.left, value) && dfs(root.right, value);
}
function isUnivalTree(root) {
  return dfs(root, root.val);
}