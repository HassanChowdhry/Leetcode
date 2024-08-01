// https://leetcode.com/problems/median-of-two-sorted-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let arr = nums1.concat(nums2);
    arr.sort((a, b) => a - b);

    let mid = (arr.length / 2) - 1;

    if (Math.floor(mid) !== Math.ceil(mid)) {
      return arr[Math.ceil(mid)];
    } else {
      let avg = (arr[mid] + arr[mid + 1]) / 2;
      return avg;
    }
};