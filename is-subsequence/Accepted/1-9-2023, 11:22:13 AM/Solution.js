// https://leetcode.com/problems/is-subsequence

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
  let arr = [];
  let prev = 0;
  
  for (let i = 0; i < s.length; i++) {
    for (let j = prev; j < t.length; j++) {
      if (s[i] === t[j]) {
        arr.push([s[i], j]);
        prev = j + 1;
        break;
      }
    }
  }

  for (let i = 0; i < arr.length - 1; i++) {
    if (s[i] !== arr[i][0] || (arr[i][1] > arr[i + 1][1])) {
      return false;
    }
  }

  return arr.length === s.length;
};