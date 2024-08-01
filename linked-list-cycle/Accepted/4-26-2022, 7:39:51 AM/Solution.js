// https://leetcode.com/problems/linked-list-cycle

/**
 * 
 * @param {TreeNode} head 
 * @param {Set?} set 
 */
function helper(head, set) {
  if (head == null) {
    return false;
  }
  
  if (set.has(head)) {
    return true;
  }
set.add(head);
  return helper(head.next, set);
}

/**
 ** Recursive - Time O(n), Space O(n)
 * @param {ListNode} head
 * @return {boolean}
 */
function hasCycle(head) {
  let set = new Set();
  return helper(head, set);
}
