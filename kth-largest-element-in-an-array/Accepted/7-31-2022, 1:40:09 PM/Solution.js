// https://leetcode.com/problems/kth-largest-element-in-an-array

function findKthLargest(nums, k) {
  nums.sort((a, b) => a - b);
  return nums[nums.length - k];
}