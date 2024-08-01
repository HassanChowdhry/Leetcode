// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
     let sortedArray = [...nums].sort((a, b) => a - b);
  let result = [];

  for (let num of nums) {
    result.push(sortedArray.indexOf(num));
  }
  return result;
}