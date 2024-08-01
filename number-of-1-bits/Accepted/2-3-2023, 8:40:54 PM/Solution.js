// https://leetcode.com/problems/number-of-1-bits

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
function hammingWeight(n) {
  if (n===0) return 0;
  return (n & 1) + hammingWeight(n >>> 1);
}