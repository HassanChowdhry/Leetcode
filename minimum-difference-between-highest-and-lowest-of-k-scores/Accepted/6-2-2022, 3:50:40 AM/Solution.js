// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if (k === 1) {
    return 0;
  }
  nums = nums.sort((a, b) => b - a);
  let minDiff = (nums[0] - nums[k- 1]);

  for (let i = 0; i < nums.length - k + 1; i++) {
    let num = nums[i] - nums[i + k - 1];
    if (minDiff > num) {
      minDiff = num;
    }
  }
  return minDiff;
};