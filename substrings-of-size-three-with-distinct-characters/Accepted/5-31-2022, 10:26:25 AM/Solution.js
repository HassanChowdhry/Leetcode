// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

/**
 * @param {string} s
 * @return {number}
 */
var countGoodSubstrings = function(s) {
   let count = 0;

  for (let i = 0; i < s.length - 2; i++) {

    if (s[i] === s[i + 1] || s[i + 1] === s[i + 2] || s[i] === s[i + 2]) {
      continue;
    }

    count++;
  }

  return count;
}