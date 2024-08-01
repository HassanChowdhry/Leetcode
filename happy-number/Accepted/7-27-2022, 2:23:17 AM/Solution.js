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
  let set = new Set();

  while (n !== 1 && !set.has(n)) {
    set.add(n);
    n = sumOfSquared(n);
  }

  return n === 1;
}