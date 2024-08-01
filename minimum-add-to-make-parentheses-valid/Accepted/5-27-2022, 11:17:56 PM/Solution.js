// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
     let openParaRegex = /\(/g;
  let closeParaRegex = /\)/g;

  if (s.search(openParaRegex) === -1 || s.search(closeParaRegex) === -1) {
   return ((s.match(closeParaRegex) || []).length > 0 ? (s.match(closeParaRegex) || []).length : (s.match(openParaRegex) || []).length)
  }

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