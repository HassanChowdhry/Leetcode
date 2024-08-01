// https://leetcode.com/problems/minimum-depth-of-binary-tree

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
var minDepth = function(root) {
    let queue = [];
  queue.push(root);
  
  let minimumDepth = 0;

  while (queue.length > 0) {
    let size = queue.length;
       minimumDepth += 1;

    for (let i = 0; i < size; i++) {
      let node = queue.shift();
      
      if (!node) {
        return 0;
      }

      if (!node.left && !node.right) {
        return minimumDepth;
      }
      
      if (node.left) {
        queue.push(node.left);
      }
      
      if (node.right) {
        queue.push(node.right);
      }
    }
   
  }
  return minimumDepth;
}

