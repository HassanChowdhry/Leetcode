// https://leetcode.com/problems/n-th-tribonacci-number

/**
 * @param {number} n
 * @return {number}
 */
function tribonacci(n, map = new Map()) {
  if (map.has(n)) {
    return map.get(n);
  }

  let result;
  if (n === 0) {
    result = 0;

  } else if (n === 1 || n === 2) {
    result = 1;
  
  } else {
    result = tribonacci(n - 3, map) + tribonacci(n - 2, map) + tribonacci(n - 1, map);
  }
  map.set(n, result);
  return result;
}