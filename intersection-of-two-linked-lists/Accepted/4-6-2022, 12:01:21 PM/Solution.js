// https://leetcode.com/problems/intersection-of-two-linked-lists

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
  if (headA === null || headB === null) {
    return null;
  }

  let hA = headA;
  let hB = headB;

  while (hA !== hB) {
    if (hA == null) {
      hA = headB;
    
    } else {
      hA = hA.next;
    }

    if (hB == null) {
      hB = headA;
    
    } else {
      hB = hB.next;
    }
  }

  return hA;
}
