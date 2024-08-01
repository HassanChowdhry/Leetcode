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
    let mergedList = new ListNode();
  let newHead = mergedList;

  let head1 = list1;
  let head2 = list2;

  while (head1 != null || head2 != null) {

    if (head1 == null) {
      newHead.next = new ListNode(head2.val);
      head2 = head2.next;

    } else if (head2 == null) {
      newHead.next = new ListNode(head1.val); 
      head1 = head1.next;

    } else if (head1.val < head2.val) {
      newHead.next = new ListNode(head1.val); 
      head1 = head1.next;

    } else {
      newHead.next = new ListNode(head2.val);
      head2 = head2.next;
    }
  
    newHead = newHead.next;
  }
  return mergedList.next;
};