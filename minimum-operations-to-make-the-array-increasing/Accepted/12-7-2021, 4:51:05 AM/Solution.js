// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
  let count = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    let difference = nums[i + 1] - nums[i];
    if (difference <= 0) {
      nums[i + 1] += Math.abs(difference) + 1;
      count += Math.abs(difference) + 1;
    }
  }
  return count;
};