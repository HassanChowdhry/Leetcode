// https://leetcode.com/problems/middle-of-the-linked-list

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
     let array = [];
  let currentNode = head;

  while (currentNode != null) {
    array.push(currentNode);
  
          currentNode = currentNode.next;
  }

  let halfArrayLength = Math.floor(array.length / 2);
  return array[halfArrayLength];
};