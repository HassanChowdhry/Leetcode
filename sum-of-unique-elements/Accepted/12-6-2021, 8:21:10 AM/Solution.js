// https://leetcode.com/problems/sum-of-unique-elements

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
      let uniqueSet = new Set();
  let dupSet = new Set();
  let sum = 0;
  
  for (let num of nums){
    if (uniqueSet.has(num))
      dupSet.add(num);
    else uniqueSet.add(num)
  }
  for (let num of uniqueSet) {
    if (dupSet.has(num))
      uniqueSet.delete(num);
    else sum += num
  }
  return sum;
};