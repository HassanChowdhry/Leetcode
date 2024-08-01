// https://leetcode.com/problems/n-ary-tree-level-order-traversal

/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
if (!root) {
    return [];
  }

  let result = [];
  let queue = [root];

  while (queue.length > 0) {

    let queueSize = queue.length;

    let row = [];

    for (let i = 0; i < queueSize; i++) {

      let node = queue.shift();

      if (node.children) {
        for (let child of node.children) {
          queue.push(child);
        }
      }

      row.push(node.val);

    }

    result.push(row);

  }

  return result;
}
