// https://leetcode.com/problems/number-of-1-bits

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
function hammingWeight(n) {
  let count = 0;
 
  while (n > 0) {
    count += (n & 1);
    n >>>= 1; // extra sign for unsigned shift
  }

  return count;
}
