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
  let set1 = new Set(); 
  let set2 = new Set(); 
  let set3 = new Set();
  
  nums1.forEach((num) => { set1.add(num); });
  nums2.forEach((num) => { set2.add(num); });
  nums3.forEach((num) => { set3.add(num); });

  for (let num of set1.values()) {
    occurMap.set(num, 1);
  }

  for (let num of set2.values()) {
    if (occurMap.has(num)) {
      occurMap.set(num, occurMap.get(num) + 1);
    } else {
      occurMap.set(num, 1);
    }
  }

  for (let num of set3.values()) {
    if (occurMap.has(num)) {
      occurMap.set(num, occurMap.get(num) + 1);
    }
  }

  for (let [key, value] of occurMap.entries()) {
    if (value > 1) {
      resArray.push(key);
    }
  }

  return resArray;
};