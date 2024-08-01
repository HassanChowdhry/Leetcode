// https://leetcode.com/problems/majority-element

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
if (nums.length === 1) return nums[0];
  
  let map = new Map();
  let max = Math.floor(nums.length / 2);

  for (let num of nums) {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
      
      if (map.get(num) > max) {
        return num;
      }
    } else {
      map.set(num, 1);
    }
  }

};