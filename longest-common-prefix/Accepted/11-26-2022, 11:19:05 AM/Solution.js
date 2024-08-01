// https://leetcode.com/problems/longest-common-prefix

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let str = '';
  let firstStr = strs[0];
  let isPrefix = true;
  
  for (let i = 0; i < firstStr.length && isPrefix; i++) {
    let char = firstStr[i];
    for (let j = 1; j < strs.length; j++) {
      if (char !== strs[j][i]) {
        isPrefix = false;
      }
    }
    if (isPrefix) str += char;
  }

  return str;
};