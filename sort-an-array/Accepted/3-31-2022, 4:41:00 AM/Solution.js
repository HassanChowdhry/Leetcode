// https://leetcode.com/problems/sort-an-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
for (let i = 0; i < nums.length; i++) {
    let min = nums[i];
    let minIndex = i;

    for (let j = i + 1; j < nums.length; j++) {
      
      if (min > nums[j]) {
        min = nums[j];
        minIndex = j;
      }
    }

    let temp = nums[i];
    nums[i] = min;
    nums[minIndex] = temp;

  }

  return nums;
}
