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
function dfs(root, leftArray) {
  if (!root) {
    return;
  }

  dfs(root.left, leftArray);
  dfs(root.right, leftArray);

  if (root.left && (!root.left.left && !root.left.right)) {
    leftArray.push(root.left.val);
  }
}
function sumOfLeftLeaves(root) {
  let leftArray = [];
  dfs(root, leftArray);

  let sum = 0;
  for (let num of leftArray) {
    sum += num;
  }

  return sum;
}
