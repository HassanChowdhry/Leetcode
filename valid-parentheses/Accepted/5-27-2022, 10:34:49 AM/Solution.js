// https://leetcode.com/problems/valid-parentheses

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(str) {
    const openRegex = /[({[]/;
  const closeRegex = /[)}\]]/;
   if (str.search(openRegex) === -1 || str.search(closeRegex) === -1 || str[0] === ')' || str[0] === '}' || str[0] === ']') {

    return false;
  }

  let bracketPairMap = new Map();
  bracketPairMap.set(')', '(');
  bracketPairMap.set('}', '{');
  bracketPairMap.set(']', '[');

  let stack = [];

  for (let i = 0; i < str.length; i++) {
    if (str[i].search(openRegex) !== -1) {
      stack.push(str[i]);
    } else {
      let openPar = stack.pop();
      if (bracketPairMap.get(str[i]) !== openPar) {
        return false;
      }
    }

    if (stack.length > 0 && i + 1 === str.length) {
      return false;
    }
  }

  return true;
};