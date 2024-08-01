// https://leetcode.com/problems/invert-binary-tree

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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    let queue = [];
  queue.push(root);

  while (queue.length > 0) {
    let size = queue.length;

    for (let i = 0; i < size; i++) {
      let node = queue.shift();
      if (!node) {
        return root;
      }
      if (node.left && !node.right) {
        queue.push(node.left);
        node.right = node.left;
        node.left = null;

      } else if (!node.left && node.right) {
        queue.push(node.right);
        node.left = node.right;
        node.right = null;

      } else {
        let temp = node.left;
        if (node.left) {
          queue.push(node.left);
          node.left = node.right;
        }

        if (node.right) {
          queue.push(node.right);
          node.right = temp;
        }
      }
    }
  }
  return root;
};