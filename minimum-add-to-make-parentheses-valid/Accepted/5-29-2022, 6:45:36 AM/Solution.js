// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
     let openParaRegex = /\(/g;
  let closeParaRegex = /\)/g;

  if (s.search(openParaRegex) === -1) {
    let closeParaCount = (s.match(closeParaRegex) || []).length; 
    return closeParaCount;
  }
  
  if (s.search(closeParaRegex) === -1) {
    let openParaCount = (s.match(openParaRegex) || []).length; 
    return openParaCount;
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