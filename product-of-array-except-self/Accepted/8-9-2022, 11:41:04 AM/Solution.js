// https://leetcode.com/problems/product-of-array-except-self

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  let prefix = [nums[0]];
  let postfix = [nums[nums.length - 1]];
  
  for (let i = 1; i < nums.length; i++) {
    let prefixOfI = nums[i] * prefix[prefix.length - 1];
    prefix.push(prefixOfI);

    let postFixOfI = nums[nums.length - i - 1] * postfix[0];
    postfix.unshift(postFixOfI);
  }
  
  for (let i = 1; i < nums.length - 1; i++) {
    nums[i] = prefix[i - 1] * postfix[i + 1];
  }
  nums.splice(0, 1, postfix[1]);
  nums.splice(nums.length - 1, 1, prefix[prefix.length - 2]);
  
  return nums;
}