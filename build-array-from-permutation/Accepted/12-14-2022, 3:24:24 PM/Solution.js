// https://leetcode.com/problems/build-array-from-permutation

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
  let len = nums.length;
  for (let i = 0; i < len; i++) {
    nums.push(nums[nums[i]]);
  }
  nums.splice(0, len);
  return nums;
};