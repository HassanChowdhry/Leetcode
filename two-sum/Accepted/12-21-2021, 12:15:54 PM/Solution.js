// https://leetcode.com/problems/two-sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
   let numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    numMap.set(nums[i], i);
  }

  for (let num of nums) {
    if (numMap.has(target - num) && (numMap.get(target - num) !== nums.indexOf(num))) {
      return [numMap.get(target - num), nums.indexOf(num)];
    }
  }

  return null;
};