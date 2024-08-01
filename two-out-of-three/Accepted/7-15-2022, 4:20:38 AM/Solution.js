// https://leetcode.com/problems/two-out-of-three

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    let resArray = [];
  let occurMap = new Map();
  let numsArray = [...new Set(nums1), ...new Set(nums2), ...new Set(nums3)];

  for (let num of numsArray) {
    if (occurMap.has(num)) {
      occurMap.set(num, occurMap.get(num) + 1);
    
    } else {
      occurMap.set(num, 1);
    }
  }

  for (let [key, value] of occurMap.entries()) {
    if (value > 1) {
      resArray.push(key);
    }
  }

  return resArray;
};