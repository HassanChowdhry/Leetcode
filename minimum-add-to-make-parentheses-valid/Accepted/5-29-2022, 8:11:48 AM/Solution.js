// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
     
   let openParCount = 0;
  let closeParCount = 0;

  for (let i = 0; i < s.length; i++) {

    if (s[i] === '(') {
      openParCount++;

    } else if (openParCount > 0) {
      openParCount--;
    
    } else {
      closeParCount++;
    }
  }

  return openParCount + closeParCount;
};