// https://leetcode.com/problems/kth-smallest-element-in-a-bst

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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
 let count = 1;
  let val;

  function dfs2(root) {
    if (!root) return root;

    dfs2(root.left);
    
    if (count === k) {
      val = root.val;
    } 
    count++;

    dfs2(root.right);
  }
  dfs2(root);

  return val;
};