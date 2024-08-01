// https://leetcode.com/problems/n-repeated-element-in-size-2n-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    
  let n = parseInt(nums.length/2);

  for (let i = 0; i < nums.length - 1; i++) {
      let count = 1;
      
      for (let j = 0; j < nums.length; j++) {
  
        if (i !== j && nums[i] === nums[j])
          count++;
      }
      if (n === count)
      return nums[i];
  }
};