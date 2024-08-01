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
   let lengthA = 0;
  let lengthB = 0;

  let hA = headA;
  let hB = headB;

  while (hA) {
    lengthA++;
    hA = hA.next;
  }
  
  while (hB) {
    lengthB++;
    hB = hB.next;
  }

  hA = headA;
  hB = headB;

  let diff = Math.abs(lengthA - lengthB);

  if (lengthA > lengthB) {
    while (diff > 0) {
      hA = hA.next;
      diff--;
    }
  
  } else {
    while (diff > 0) {
      hB = hB.next;
      diff--;
    }
  }

  while (hA !== hB) {
    hA = hA.next;
    hB = hB.next;
    
    if (hA == null || hB == null) {
      return null;
    }
  }

  return hA;
}
