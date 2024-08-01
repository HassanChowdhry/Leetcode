// https://leetcode.com/problems/build-array-from-permutation

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
  for (let i = 0; i < nums.length / 2; i++) {
    nums.push(nums[nums[i]]);
  }
  nums.splice(0, nums.length / 2);
  return nums;
};