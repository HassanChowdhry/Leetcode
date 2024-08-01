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
    let count = 0;
  let currentNode = head;
  let halfCount = 0;

  while (currentNode != null) {
    count++;
    currentNode = currentNode.next;
  }

  while (head != null) {
    if (halfCount === Math.floor(count / 2) ) {
      return head;
    }
    halfCount++;
    head = head.next;
  }
    }