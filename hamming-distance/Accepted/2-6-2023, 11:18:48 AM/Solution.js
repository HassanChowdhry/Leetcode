// https://leetcode.com/problems/hamming-distance

/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
  return x === 0 && y === 0 ? 0 : ((x & 1) ^ (y & 1)) + hammingDistance(x >>> 1, y >>> 1);
};