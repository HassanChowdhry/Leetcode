// https://leetcode.com/problems/climbing-stairs

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n, map = new Map()) {
if (map.has(n)) {
    return map.get(n);
  }
  
  let result;
  if (n <= 2) {
    result = n;
  } else {
    result = climbStairs(n - 2, map) + climbStairs(n - 1, map);
  }
  map.set(n, result);
  return result;
};