// https://leetcode.com/problems/median-of-two-sorted-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let n = 0;
  let m = 0;
  let arr = [];

  while (n < nums1.length && m < nums2.length) {
    if (nums1[n] < nums2[m]) {
      arr.push(nums1[n]);
      n++;
    } else {
      arr.push(nums2[m]);
      m++;
    }
  }

  while (n < nums1.length) {
    arr.push(nums1[n]);
    n++;
  }

  while (m < nums2.length) {
    arr.push(nums2[m]);
    m++;
  }

  let mid = (arr.length / 2) - 1;

  if (Math.floor(mid) !== Math.ceil(mid)) {
    return arr[Math.ceil(mid)];
  } 
  let avg = (arr[mid] + arr[mid + 1]) / 2;
  return avg;
};