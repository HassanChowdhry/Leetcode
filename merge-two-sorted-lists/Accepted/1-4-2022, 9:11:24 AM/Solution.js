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
    let sortedList = new ListNode();
  let newHead = sortedList;

  let head1 = list1;
  let head2 = list2;

  while (head1 != null || head2 != null) {

    if (head1 == null) {
      sortedList.next = new ListNode(head2.val);
      head2 = head2.next;

    } else if (head2 == null) {
      sortedList.next = new ListNode(head1.val); 
      head1 = head1.next;

    } else if (head1.val < head2.val) {
      sortedList.next = new ListNode(head1.val); 
      head1 = head1.next;

    } else {
      sortedList.next = new ListNode(head2.val);
      head2 = head2.next;
    }
  
    sortedList = sortedList.next;
  }
  return newHead.next;
};