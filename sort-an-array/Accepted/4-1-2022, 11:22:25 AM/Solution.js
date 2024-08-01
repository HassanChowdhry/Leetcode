// https://leetcode.com/problems/sort-an-array

/**
 * 
 * @param {number[]} array 
 * @param {number[]} left 
 * @param {number[]} right 
 */
function merge(array, left, right) {

  while (left.length > 0 && right.length > 0) {
    if (left[0] > right[0]) {
      array.push(right.shift());
    
    } else {
      array.push(left.shift());
    }
  }

  while (left.length > 0) {
    array.push(left.shift());  
  }

  while (right.length > 0) {
    array.push(right.shift());  
  }

  return array;
}

/**
 * ! Merge
 * * Time O(nlogn), Space O(1)
 * @param {number[]} nums 
 * @returns {number[]}
 */
function sortArray(nums) {

  let len = nums.length;

  if (len <= 1) {
    return nums;
  } 

  let middle = Math.floor(len / 2);
  let left = [];
  let right = [];

  for (let i = 0; i < middle; i++) {
    left.push(nums.shift());
  } 

  for (let j = middle; j < len; j++) {
    right.push(nums.shift());
  }

  sortArray(left);
  sortArray(right);
  merge(nums, left, right);
  
  return nums;
}
