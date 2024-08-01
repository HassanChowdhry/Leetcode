// https://leetcode.com/problems/house-robber

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let prev1 = 0;
  let prev2 = 0;

  for (let num of nums) {
    let temp = prev1;
    prev1 = Math.max(num + prev2, prev1);
    prev2 = temp;
  }

  return prev1;
};