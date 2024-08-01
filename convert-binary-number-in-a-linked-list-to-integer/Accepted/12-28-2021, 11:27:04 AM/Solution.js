// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
     let decValue = 0;
  let currentNode = head;
  let length = 0;

  while (currentNode != null) {
    length++;

    currentNode = currentNode.next;
  }

  for (let i = length - 1; head != null; i--) {
    if (head.val !== 0) {
      decValue += (2 ** i);
    }
    
    head = head.next;
  }
  
  return decValue;
};