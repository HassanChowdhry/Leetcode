// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
     
    let stack = [];
  let num = 0;

  for (let i = 0; i < s.length; i++) {

    if (s[i] === '(') {
      stack.push(s[i]);
      num++;
    
    } else {
      let par = stack.pop();
      if (par === '(') {
        num--;
      } else {
        stack.push(s[i]);
        num++;
      }
    }
  }

  return num;
};