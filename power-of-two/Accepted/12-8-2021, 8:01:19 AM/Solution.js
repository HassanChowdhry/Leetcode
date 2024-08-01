// https://leetcode.com/problems/power-of-two

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
     while (n >= 1) {
    if (n === 1) {
      return true;
    }
    n /= 2;
  }
  return false;
};