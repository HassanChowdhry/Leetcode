// https://leetcode.com/problems/array-partition

/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort((a, b) => a - b);
  let sum = 0;

  while (nums.length) {
    sum += Math.min(nums.pop(), nums.pop());
  }

  return sum;
};