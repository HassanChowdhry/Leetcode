// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
  let stack = [];

  for (let c of s) {
    if (stack.length > 0 && stack[stack.length - 1][0] === c) {
      stack[stack.length - 1][1] += 1;
    } else {
      stack.push([c, 1]);
    } 

    if (stack.length > 0 && stack[stack.length - 1][1] === 2) {
      stack.pop();
    }
  }
  
  let res = '';

  for (let value of stack) {
    res += value[0].repeat(value[1]);
  }

  return res;
};