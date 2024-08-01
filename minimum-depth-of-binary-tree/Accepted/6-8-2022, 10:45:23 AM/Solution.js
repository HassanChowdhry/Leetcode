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
function minDepth(root, map = new Map()) {
  if (map.has(root)) {
    return map.get(root);
  }
  if (!root) {
    return 0;
  }
  
  let depth;
  if (root.left && !root.right) {
    depth = 1 + minDepth(root.left);
  
  } else if (root.right && !root.left) {
    depth = 1 + minDepth(root.right);
  
  } else {
    depth = 1 + Math.min(minDepth(root.left), minDepth(root.right));
  }
  map.set(root, depth);
  return depth;
}
