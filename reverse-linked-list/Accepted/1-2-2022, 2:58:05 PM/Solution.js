// https://leetcode.com/problems/reverse-linked-list

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
var reverseList = function(head) {
     let currentNode = head;
  let reversehead = head;
  let stack = [];
 
  while (currentNode != null) {
    stack.push(currentNode.val);

    currentNode = currentNode.next;
  }
  while (reversehead != null) {
    reversehead.val = stack.pop();

    reversehead = reversehead.next;
  }

  return head;
};