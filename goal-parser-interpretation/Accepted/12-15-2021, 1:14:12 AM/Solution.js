// https://leetcode.com/problems/goal-parser-interpretation

/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    let result = '';

  for (let i = 0; i < command.length; i++) {
    if (command.charAt(i) === 'G') { 
      result += 'G'; 
    } else if (command.charAt(i) === '(' && command.charAt(i + 1) === 'a') {
      result += 'al';
    } else if (command.charAt(i) === '(' && command.charAt(i + 1) === ')') { 
      result += 'o'; 
    }
  }
  return result;
};