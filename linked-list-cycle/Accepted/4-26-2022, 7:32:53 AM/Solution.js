// https://leetcode.com/problems/linked-list-cycle

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let set = new Set();
  let currNode = head;

  while (currNode != null) {

    if (set.has(currNode)) {
      return true;
    }
    set.add(currNode);
    
    currNode = currNode.next;
  }

  return false;
};