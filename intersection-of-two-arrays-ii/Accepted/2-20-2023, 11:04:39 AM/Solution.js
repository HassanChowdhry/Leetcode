// https://leetcode.com/problems/intersection-of-two-arrays-ii

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
  let res = [];
  let map1 = new Map();
  let map2 = new Map();

  for (let num of nums1) {
    if (map1.has(num)) {
      map1.set(num, map1.get(num) + 1);
    } else {
      map1.set(num, 1);
    }
  }

  for (let num of nums2) {
    if (map2.has(num)) {
      map2.set(num, map2.get(num) + 1);
    } else {
      map2.set(num, 1);
    }
  }

  for (let [key, value] of map1) {
    if (map2.has(key)) {
      let iter = value <= map2.get(key) ? value : map2.get(key);
      for (let i = 0; i < iter; i++) {
        res.push(key);
      }
    }
  }

  return res;
};