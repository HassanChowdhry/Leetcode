// https://leetcode.com/problems/hamming-distance

/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
      let count = 0;

  for (let num = x ^ y; num > 0; num >>>= 1) {
    if (num & 1) count++; // if last bit was one add to counter
  }

  return count;
};