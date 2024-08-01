// https://leetcode.com/problems/fibonacci-number

/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
     if (n === 0 || n === 1) {
    return n;
  }

  let map = new Map();
  map.set(0, 0);
  map.set(1, 1);
  for (let i = 2; i <= n; i++) {
    map.set(i, (map.get(i - 2) + map.get(i - 1)));
  }
  return map.get(n);
};