// https://leetcode.com/problems/intersection-of-two-arrays-ii

// https://leetcode.com/problems/intersection-of-two-arrays-ii/

/**
 * Time O(n + m), Space O(n)
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
function intersect(nums1, nums2) {
  let res = [];
  let map1 = new Map();
  let map2 = new Map();
 
  // sets nums1 into a map1
  for (let num of nums1) {
    map1.set(num, (map1.get(num) ?? 0) + 1);
  }

  // sets nums1 into a map2
  for (let num of nums2) {
    map2.set(num, (map2.get(num) ?? 0) + 1);
  }

  // adds intersected numbers into an array, even duplicates
  for (let [key, value] of map1) {
    if (map2.has(key)) {
      let iter = value <= map2.get(key) ? value : map2.get(key);
      for (let i = 0; i < iter; i++) {
        res.push(key);
      }
    }
  }

  return res;
}
