// https://leetcode.com/problems/number-of-1-bits

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
function hammingWeight(n) {
   return n === 0 ? 0 : ((n & 1) + hammingWeight(n >>> 1));

}
