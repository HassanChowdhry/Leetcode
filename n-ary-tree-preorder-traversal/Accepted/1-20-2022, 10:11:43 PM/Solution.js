// https://leetcode.com/problems/n-ary-tree-preorder-traversal

/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
function dfs(root, resultArray) {
  if (!root) {
    return;
  }
  resultArray.push(root.val);
  for (let node of root.children) {
    dfs(node, resultArray);
  }
}
function preorder(root) {
  let array = [];
  dfs(root, array);
  return array;
}