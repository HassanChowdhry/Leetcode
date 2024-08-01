// https://leetcode.com/problems/power-of-two

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(num) {
   if (num === 1) {
    return true;
  }
  if (num < 1) {
    return false;
  }
  return isPowerOfTwo(num / 2);
};