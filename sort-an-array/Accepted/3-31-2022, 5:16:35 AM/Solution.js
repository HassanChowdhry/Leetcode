// https://leetcode.com/problems/sort-an-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
for (let i = 1; i < nums.length; i++) {

    for (let j = 0; j < i; j++) {

      if (nums[i] < nums[j]) {
        
        let temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
      }
    }
  }
  return nums;
}
