// https://leetcode.com/problems/binary-tree-preorder-traversal

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
function dfs(root, resultArray) {
  if (!root) {
    return;
  }
  resultArray.push(root.val);
  dfs(root.left, resultArray);
  dfs(root.right, resultArray);
}

function preorderTraversal(root) {
  let array = [];
  dfs(root, array);
  return array;
}