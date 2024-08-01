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

 for (let i = 0; i < sqArray.length; i++) {
    let max = sqArray[i];
    let indexOfMax = i;

    for (let j = i + 1; j < sqArray.length; j++) {
      if (sqArray[j] > max) {
        max = sqArray[j];
        indexOfMax = j;
      }
    }
    sqArray.splice(indexOfMax, 1);
    sqArray.unshift(max);
  }
  
    return sqArray;
};