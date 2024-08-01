// https://leetcode.com/problems/valid-parentheses

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(str) {
    let bracketPairMap = new Map();
  bracketPairMap.set('(', ')');
  bracketPairMap.set('{', '}');
  bracketPairMap.set('[', ']');


  let stack = [];

  for (let c of str) {
    if (bracketPairMap.has(c)) {
      stack.push(c);
    
    } else if (stack.length !== 0) {
      let openPar = stack.pop();
      if (bracketPairMap.get(openPar) !== c) {
        return false;
      }

    } else {
      return false;
    }
  }

  return (stack.length === 0);
};