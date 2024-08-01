// https://leetcode.com/problems/missing-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let numSet = new Set();

  nums.forEach((num) => {
    numSet.add(num);
  });

  for (let i = 0; i < nums.length + 1; i++) {
    if (!numSet.has(i)) {
      return i;
    }
  }
};