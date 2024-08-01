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

  let res = [[root.val]];
  let queue = [[root]];

  while (queue.length > 0) {
    let nodeArray = queue.shift();

    let childValueArray = [];
    let childNodeArray = [];

    for (let i = 0; i < nodeArray.length; i++) {
    
      if (nodeArray[i].children) {
    
        for (let child of nodeArray[i].children) {
          childNodeArray.push(child);
          childValueArray.push(child.val);
        }
      }
    }

    if (childNodeArray.length > 0) {
      queue.push(childNodeArray);
    }
    
    if (childValueArray.length > 0) {
      res.push(childValueArray);
    }
    
  }

  return res;
}
