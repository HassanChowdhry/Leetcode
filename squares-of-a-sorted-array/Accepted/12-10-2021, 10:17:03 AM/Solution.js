// https://leetcode.com/problems/squares-of-a-sorted-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  let start = 0;
  let end = nums.length - 1;
  let sqNums = [];
  for (let i = 0; i < nums.length; i++) {
    if (Math.abs(nums[start]) <= Math.abs(nums[end])) {
      sqNums.unshift(nums[end] * nums[end]);
      end--;
    } else {  
      sqNums.unshift(nums[start] * nums[start]);
      start++;
    }
  }
  return sqNums;
}

