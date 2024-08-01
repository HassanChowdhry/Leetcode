// https://leetcode.com/problems/average-of-levels-in-binary-tree

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
var averageOfLevels = function(root) {
    let queue = []; 
  let res = [];
  queue.push(root);

  while (queue.length > 0) {
    let size = queue.length;
    let sum = 0;

    for (let i = 0; i < size; i++) {
      let node = queue.shift();

      if (node.left) {
        queue.push(node.left);
      }
      
      if (node.right) {
        queue.push(node.right);
      }
    
      sum += node.val;
    }

    res.push(sum / size);
  }
  
  return res;
};