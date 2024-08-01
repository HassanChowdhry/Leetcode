// https://leetcode.com/problems/remove-duplicates-from-sorted-list

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
var deleteDuplicates = function(head) {
    let temp = head;
    while (temp !== null) {
      let curr = temp;
      while (curr !== null && curr.next !== null) {
        if (curr.next.val === temp.val) {
          curr.next = curr.next.next;
        } else {
          curr = curr.next;
        }
      }
      temp = temp.next
    }

    return head;
};