// https://leetcode.com/problems/contains-duplicate

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let dupSet = new Set();

  for (let i = 0; i < nums.length; i++) {
    if (dupSet.has(nums[i])) {
      return true;
    }
    dupSet.add(nums[i]);
  }
  return false;
};