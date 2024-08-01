// https://leetcode.com/problems/hamming-distance

/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
   let num = x ^ y; // xor gives 1 in each diff bit placement
  let count = 0;

  while (num > 0) {
    if (num & 1) count++;
    num >>>= 1;
  }

  return count;
};