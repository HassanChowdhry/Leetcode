// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    if (num === 0) {
    return 0;
  }
  if (num % 2 === 0) {
    return 1 + numberOfSteps(parseInt(num / 2));
  }
  return 1 + numberOfSteps(num - 1);
};