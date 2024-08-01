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
function dfs(root, array) {
  if (!root) {
    return array;
  }
  dfs(root.left, array);
  array.push(root.val);
  return dfs(root.right, array);
}

function inorderTraversal(root) {
  return dfs(root, []);
}
