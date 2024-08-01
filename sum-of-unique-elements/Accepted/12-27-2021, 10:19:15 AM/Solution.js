// https://leetcode.com/problems/sum-of-unique-elements

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
  let uniqueSet = new Set();
  let dupSet = new Set();
  let sum = 0;

  nums.forEach((num) => {
    if (uniqueSet.has(num)) {
      dupSet.add(num);
    } else {
      uniqueSet.add(num);
    }
  });

  for (let num of uniqueSet) {
    if (!dupSet.has(num)) {
      sum += num;
    }
  }

  return sum;
}