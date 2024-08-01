// https://leetcode.com/problems/sum-of-unique-elements

/**
 * @param {number[]} nums
 * @return {number}
 */
function sumOfUnique(nums) { 

 
  let numMap = new Map();
  let sum = 0;

  for (let c of nums) {
    if (numMap.has(c))
       numMap.set(c, numMap.get(c) + 1);
  else numMap.set(c, 1);  
  }

 for (let [key, value] of numMap.entries()) {
    if (value === 1)
      sum += key;
  }
  return sum;
};