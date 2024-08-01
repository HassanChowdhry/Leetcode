// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function(s, k) {
   let stack = [[s[0], 1]];

  for (let c = 1; c < s.length; c++) {
    let prev = stack.pop();

    if (prev && prev[0] === s[c]) {
      prev[1] += 1;
    }  
    
    if (prev && prev[1] !== k) {
      stack.push(prev);
    }

    if (!prev || prev[0] !== s[c]) {
      stack.push([s[c], 1]);
    } 
  }
  let res = '';

  for (let value of stack) {
    res += value[0].repeat(value[1]);
  }

  return res;
}