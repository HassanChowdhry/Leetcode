// https://leetcode.com/problems/fibonacci-number

function fib(n, map = new Map()) {
  if (map.has(n)) {
    return map.get(n);
  }

  let result;
  if (n === 1) {
    result = 1;
  } else if (n === 0) {
    result = 0;
  } else {
    result = fib(n - 2, map) + fib(n - 1, map);
  }
  map.set(n, result);
  return result;
}