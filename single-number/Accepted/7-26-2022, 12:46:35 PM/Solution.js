// https://leetcode.com/problems/single-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
 return nums.reduce((prev,curr) => prev ^ curr )
}