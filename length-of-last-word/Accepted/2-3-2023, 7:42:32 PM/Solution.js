// https://leetcode.com/problems/length-of-last-word

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let arr = s.split(" ");
    for (let i = arr.length; i > 0; i--) {
      if (arr[i - 1].length > 0) {
        return arr[i - 1].length;
      }
    }
};