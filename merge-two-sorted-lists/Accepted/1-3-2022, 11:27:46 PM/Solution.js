// https://leetcode.com/problems/merge-two-sorted-lists

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let queue = [];
  let head1 = list1;
  let head2 = list2;

  let emptyCase = list1;

  while (head1 != null || head2 != null) {

    if (head1 == null) {
      queue.push(head2.val);
      head2 = head2.next;

    } else if (head2 == null) {
      queue.push(head1.val);
      head1 = head1.next;

    } else if (head1.val < head2.val) {
      while (head1 != null && head1.val <= head2.val) {
        queue.push(head1.val);
        head1 = head1.next;

      }
      queue.push(head2.val);
      head2 = head2.next;

    } else if (head1.val >= head2.val) {
      while (head2 != null && head2.val <= head1.val) {
        queue.push(head2.val);
        head2 = head2.next;
      }
      queue.push(head1.val);
      head1 = head1.next;

    }
  }
  if (queue.length === 0) {
    return emptyCase;
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