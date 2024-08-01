// https://leetcode.com/problems/sort-array-by-increasing-frequency

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
   let freqMap = new Map();
  for (let c of nums) {
    if (freqMap.has(c)) { 
      freqMap.set(c, freqMap.get(c) + 1); 
    } else freqMap.set(c, 1); 
  }
  
  nums.sort((a, b) => freqMap.get(a) - freqMap.get(b) || b - a ); 
  return nums;
}