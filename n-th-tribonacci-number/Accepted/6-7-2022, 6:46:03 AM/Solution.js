// https://leetcode.com/problems/n-th-tribonacci-number

/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
  if (n === 0) return 0;
  if (n === 1 || n === 2) return 1;

  let array = [0, 1, 1];
  let sum;

  for (let i = 3; i <= n; i++) {
    sum = array[i - 3] + array[i - 2] + array[i - 1];
    array.push(sum); 
  }

  return sum;
};