// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function(s, k) {
    let stack = [];

  for (let c of s) {
    if (stack.length > 0 && stack[stack.length - 1][0] === c) {
      stack[stack.length - 1][1] += 1;
    } else {
      stack.push([c, 1]);
    } 

    if (stack.length > 0 && stack[stack.length - 1][1] === k) {
      stack.pop();
    }
  }

  let str = '';

  for (let value of stack) {
    str += value[0].repeat(value[1]);
  }

  return str;
}
