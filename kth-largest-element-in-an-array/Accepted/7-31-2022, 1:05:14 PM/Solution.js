// https://leetcode.com/problems/kth-largest-element-in-an-array

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    nums.sort((a, b) => b - a);
  
  for (let num of nums) {
    k--;
    if (k === 0) {
      return num;
    }

  }
};