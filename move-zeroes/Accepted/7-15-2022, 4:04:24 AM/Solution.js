// https://leetcode.com/problems/move-zeroes

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let zeroCount = 0;
 
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      zeroCount++;
      nums.splice(i, 1);
      i--;
    }
  } 

  while (zeroCount > 0) {
    nums.push(0);
    zeroCount--;
  }

  return nums;
};