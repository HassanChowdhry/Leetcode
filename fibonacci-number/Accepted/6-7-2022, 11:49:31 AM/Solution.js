// https://leetcode.com/problems/fibonacci-number

/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n, array = []) {
   if (n === 1) {
    return 1;
  }
  
  if (n === 0) {
    return 0;
  }

  return fib(n - 2, array) + fib(n - 1, array);
};