// https://leetcode.com/problems/goal-parser-interpretation

/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
return command.replace(/\(\)/g, 'o').replace(/[()]/g, '');
};