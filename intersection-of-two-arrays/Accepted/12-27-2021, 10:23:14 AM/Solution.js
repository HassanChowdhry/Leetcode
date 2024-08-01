// https://leetcode.com/problems/intersection-of-two-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
     const resultSet = new Set();
  const set1 = new Set();


  nums1.forEach((num) => {
   set1.add(num); 
  });

  nums2.forEach((num) => {
    if (set1.has(num)) {
      resultSet.add(num); 
    }
  });


  const result = [];
  for (const num of resultSet.values()) { 
    result.push(num); 
  }

  return result;


};