// https://leetcode.com/problems/add-digits

/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
  if (num >= 10 && num % 9 === 0) return 9;
  return (num < 10 ? num : num % 9);
};