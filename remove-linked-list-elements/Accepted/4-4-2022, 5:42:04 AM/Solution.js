// https://leetcode.com/problems/remove-linked-list-elements

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
  if (!head) {
    return head;
  }
  
  let currentNode = head;
  let prev = null;

  while (currentNode) {

    if (currentNode.val === val) {
      if (prev === null) {
        currentNode = currentNode.next;
        head = currentNode;

      } else {
        prev.next = currentNode.next;
        currentNode = currentNode.next;
      }

    } else {
      prev = currentNode;
      currentNode = currentNode.next;
    }
  }
  return head;
}
