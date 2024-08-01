// https://leetcode.com/problems/binary-search

/**
 * * Time O(logn), Space O(1)
 * @param {number[]} nums 
 * @param {number} target 
 * @param {number} start 
 * @param {number} end 
 * @returns 
 */
function binarySearch(nums, target, start, end) {
  
  if (start > end) {
    return -1;
  }
  
  let middle = Math.floor((start + end) / 2);

  if (nums[middle] === target) {
    return middle;
  }

  if (nums[middle] > target) {
    return binarySearch(nums, target, start, middle - 1);
  }
  return binarySearch(nums, target, middle + 1, end);
}

/**
 * * Time O(logn), Space O(1)
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
function search(nums, target) {
  return binarySearch(nums, target, 0, nums.length);
}
