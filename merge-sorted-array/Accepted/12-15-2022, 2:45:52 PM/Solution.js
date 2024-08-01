// https://leetcode.com/problems/merge-sorted-array

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
  let i = 0;
  let j = 0;

  while (j < n) {
    if (nums1[i] < nums2[j] && i < (m + j)) {
      i++;
    } else {
      nums1.pop();
      nums1.splice(i, 0, nums2[j]);
      j++;
      i++;
    }
  }
};