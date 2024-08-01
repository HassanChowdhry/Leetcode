// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
   let numMap = new Map();

  for (let n of nums) {
    if (numMap.has(n))
      return n;
    else 
      numMap.set(n, 1);
  }
};