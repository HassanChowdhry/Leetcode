// https://leetcode.com/problems/n-ary-tree-postorder-traversal

/**
 * // Definition for a Node.
 * function Node(val,children) {
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
  for (let node of root.children) {
    dfs(node, resultArray);
  }
  resultArray.push(root.val);
}
function postorder(root) {
  let array = [];
  dfs(root, array);
  return array;
}