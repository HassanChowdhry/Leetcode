// https://leetcode.com/problems/squares-of-a-sorted-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
   let start = 0;
  let end = nums.length - 1;
  let sqNums = [];
  for (let i = nums.length - 1; i >= 0; i--) {
    if (Math.abs(nums[start]) <= Math.abs(nums[end])) {
      sqNums[i] = (nums[end] * nums[end]);
      end--;
    } else {  
      sqNums[i] = (nums[start] * nums[start]);
      start++;
    }
  }
  return sqNums;
}