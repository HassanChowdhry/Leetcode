// https://leetcode.com/problems/symmetric-tree

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
var isSymmetric = function(root) {
   if (!root) {
    return true;
  }
  let queue = [root.left, root.right];

  while (queue.length > 0) {

    let size = queue.length;
    let half = Math.floor(size / 2);
  
    for (let i = 0; i < half; i++) {
      let left = queue[i];
      let right = queue[size - i - 1];

      if (!left && !right) {
        continue;
      }

      if (!left || !right) {
        return false;
      }

      if (left.val !== right.val) {
        return false;
      }
    }

    while (size > 0) {
      let node = queue.shift();

      if (node) {
        queue.push(node.left);
        queue.push(node.right);
      }
      size--;
    }
  }
  return true;
}
