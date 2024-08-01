// https://leetcode.com/problems/number-of-1-bits

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
function hammingWeight(n) {
  let count = 0;

  for (let i = 0; i < 32; i++) {
    count += (n & 1);
    n >>= 1;
  }

  return count;
}
