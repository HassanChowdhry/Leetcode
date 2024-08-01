// https://leetcode.com/problems/palindrome-number

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) return false;
  let reverse = 0;
  let check = x;
  let count = 0;

  while (check > 0) {
    reverse = (reverse * 10) + (check % 10);
    check = Math.floor(check / 10);
    count++;
  }
  return reverse === x;
};