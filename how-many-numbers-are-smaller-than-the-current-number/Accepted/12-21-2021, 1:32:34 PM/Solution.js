// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
  let sorted = [...nums].sort((a, b) => a - b);
  let result = [];
  let map = new Map();

  sorted.forEach((num, i) => {
    if (!map.has(num)) {
      map.set(num, i);
    }
  });
  
  nums.forEach((num) => result.push(map.get(num)));

  return result;
}
