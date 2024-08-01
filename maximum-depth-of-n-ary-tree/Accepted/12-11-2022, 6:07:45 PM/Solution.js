// https://leetcode.com/problems/maximum-depth-of-n-ary-tree

/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number}
 */
var maxDepth = function(root, arr=[0]) {
    if (!root) return 0;

  let queue = [root];
  let length = 0;

  while (queue.length > 0) {
    let size = queue.length;
    for (let i = 0; i < size; i++) {
      let node = queue.shift();

      if (node.children) {
        for (let child of node.children) {
          queue.push(child);
        }
      }
    }
    length += 1;
  }

  return length;
};