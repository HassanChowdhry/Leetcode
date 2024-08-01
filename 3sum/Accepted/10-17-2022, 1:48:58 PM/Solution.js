// https://leetcode.com/problems/3sum

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let res = [];
  nums = nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && (nums[i] === nums[i - 1])) {
      continue;
    }
    let left = i + 1;
    let right = nums.length - 1;
    
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        let array = [nums[i], nums[left], nums[right]];
        res.push(array);
        left++;

        while (nums[left] === nums[left - 1] && left < right) {
          left += 1;
        }
        
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return res;
};