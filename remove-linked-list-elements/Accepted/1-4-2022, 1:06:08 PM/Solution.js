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
     
    if(!head) {
        return head;
    }

    let queue = [];
  let currentNode = head;
  while (currentNode != null) {
    queue.push(currentNode.val);
    currentNode = currentNode.next;
  }
  

  queue = queue.filter((value) => value !== val);
    if (queue.length === 0) {
        return currentNode;
}

  let newHead = new ListNode(queue.shift(), null);
  let prev = newHead;
  let current = null;

  while (queue.length > 0) {
    current = new ListNode(queue.shift(), null);
    prev.next = current;
    prev = prev.next;
  }

  return newHead;
};