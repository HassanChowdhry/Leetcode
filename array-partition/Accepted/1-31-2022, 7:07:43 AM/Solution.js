// https://leetcode.com/problems/array-partition

/**
 * @param {number[]} nums
 * @return {number}
 */
function helper(nums) {
  if (!nums.length) {
    return 0;
  } 
  let pairSum = Math.min(nums.pop(), nums.pop());
  return pairSum + helper(nums);
}
function arrayPairSum(nums) {
  nums.sort((a, b) => a - b);
  
  return helper(nums);
}