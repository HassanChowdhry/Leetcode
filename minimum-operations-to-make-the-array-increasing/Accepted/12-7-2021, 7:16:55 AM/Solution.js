// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
 let count = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    let difference = nums[i] - nums[i + 1];
    if (difference >= 0) {
      nums[i + 1] += difference + 1;
      count += difference + 1;
    }
  }
  return count;
};