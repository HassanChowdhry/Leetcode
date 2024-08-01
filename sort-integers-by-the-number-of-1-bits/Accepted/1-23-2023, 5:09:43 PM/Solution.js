// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

/**
 * 
 * @param {number} num 
 * @returns {number}
 */
function numBits(num) {
  if (num === 0) return num;
  return (num & 1) + (numBits(num >> 1));
}
/**
 * @param {number[]} arr
 * @return {number[]}
 */
function sortByBits(arr) {
  arr.sort((a, b) => (numBits(a) - numBits(b) || a - b));
  return arr;
}
