// https://leetcode.com/problems/valid-parentheses

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let map = new Map();
  map.set('{', '}');
  map.set('(', ')');
  map.set('[', ']');

  let count = 0;
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      count++;
      stack.push(s[i]);
    } else if (map.get(stack.pop()) === s[i]) {
      count--;
    } else {
      return false;
    }
    if (count < 0) return false;
  }
  return count === 0;
  };