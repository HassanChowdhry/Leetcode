// https://leetcode.com/problems/intersection-of-two-linked-lists

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * * Time O(m + n), Space O(n)
* @param {ListNode} headA
* @param {ListNode} headB
* @return {ListNode}
*/
function getIntersectionNode(headA, headB) {
  let setA = new Set();

  let hA = headA;
  let hB = headB;

  while (hA) {
    setA.add(hA);
    hA = hA.next;
  } 

  while (hB) {

    if (setA.has(hB)) {
      return hB;
    }
    hB = hB.next;
  }

  return null;
} 
