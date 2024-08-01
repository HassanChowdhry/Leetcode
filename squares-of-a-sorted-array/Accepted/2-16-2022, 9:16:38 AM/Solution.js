// https://leetcode.com/problems/squares-of-a-sorted-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  let sqArray = [];

  for (let num of nums) {
    sqArray.push(num * num);
  }
  sqArray.sort((a, b) => a - b);
  return sqArray;
};