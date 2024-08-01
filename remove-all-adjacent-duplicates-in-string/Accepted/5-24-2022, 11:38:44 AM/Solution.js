// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
   let stack = [];

  stack.push(s[0]);
  for (let i = 1; i < s.length; i++) {
    if (stack[stack.length - 1] === s[i]) {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }
  return stack.join('');
};