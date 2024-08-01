// https://leetcode.com/problems/peak-index-in-a-mountain-array

function helper(array, start, end) {

  let middle = Math.floor((start + end) / 2);

  if (array[middle] > array[middle - 1] && array[middle] > array[middle + 1]) {
    return middle;
  }

  if (array[middle] < array[middle - 1]) {
    return helper(array, start, middle - 1);
  }
  
  return helper(array, middle + 1, end);
  
}
/**
 * @param {number[]} arr
 * @return {number}
 */
function peakIndexInMountainArray(arr) {
  return helper(arr, 0, arr.length);  
}
