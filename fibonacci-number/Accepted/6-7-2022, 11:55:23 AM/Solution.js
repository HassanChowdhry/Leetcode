// https://leetcode.com/problems/fibonacci-number

/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n, map = new Map()) {
    if (map.has(n)) {
    return map.get(n);
  }

  let result;
  if (n === 1) {
    result = 1;

  } else if (n === 0) {
    result = 0;
  
  } else {
    result = fib(n - 2) + fib(n - 1);
  }
  map.set(n, result);
  return result;
};