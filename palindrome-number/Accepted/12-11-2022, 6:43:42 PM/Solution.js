// https://leetcode.com/problems/palindrome-number

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
       if (x < 0) return false;

  let arr = [];
  let count = x;

  while (count > 0) {
    arr.push(count % 10);
    count = Math.floor(count / 10);
  }

  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) return false;

    left++;
    right--;
  }
  return true;
};