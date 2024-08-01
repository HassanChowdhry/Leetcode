// https://leetcode.com/problems/happy-number

/**
 * 
 * @param {number} n 
 * @returns {number}
 */
function sumOfSquared(n) {
  let nums = [...`${n}`];
  nums = nums.map((num) => num ** 2); 
  return nums.reduce((prev, curr) => prev + curr);
}

/**
 * @param {number} n
 * @return {boolean}
 */
function isHappy(n) {
  let map = new Map();

  while (n !== 1 && !map.has(n)) {
    map.set(n, 1);
    n = sumOfSquared(n);
  }

  return n === 1;
}