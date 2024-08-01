// https://leetcode.com/problems/fibonacci-number

/**
 * @param {number} n
 * @return {number}
 */
function fib(n, array = []) {
  if (array[n] != null) {
    return array[n];
  }

  let result;
  if (n === 1) {
    result = 1;

  } else if (n === 0) {
    result = 0;
  
  } else {
    result = fib(n - 2) + fib(n - 1);
  }
  array[n] = result;
  return result;
}