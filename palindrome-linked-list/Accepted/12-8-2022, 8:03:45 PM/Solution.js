// https://leetcode.com/problems/palindrome-linked-list

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let len = 0;
    let arr = [];

    let curr = head;

    while (curr) {
        len += 1 ;
        arr.push(curr.val);
        curr = curr.next;
    }

    let left = 0;
    let right = len - 1;

    while (left < right) {
        if (arr[left] !== arr[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
};