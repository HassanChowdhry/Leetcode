// https://leetcode.com/problems/missing-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
let xor = 0;

  for (let i = 0; i <= nums.length; i++) {
    xor ^= i;
    xor ^= nums[i];
  }

  return xor;
};
