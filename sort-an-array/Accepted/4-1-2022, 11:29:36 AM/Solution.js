// https://leetcode.com/problems/sort-an-array

/**
 *? Time O(n), Space O(1)
 *
 * @param {Any[]} array 
 * @param {Number} start 
 * @param {Number} end 
 */
function partition(array, start, end) {
  let pivot = array[end];
  let pIndex = start;

  for (let i = start; i < end; i++) {

    if (array[i] <= pivot) {

      [array[i], array[pIndex]] = [array[pIndex], array[i]];
      pIndex += 1;
    }
  }

  [array[pIndex], array[end]] = [array[end], array[pIndex]];
  return pIndex;
}

/**
 ** Time: Worst case O(n^2), Average case O(nlogn), Space: O(1)
 *
 * @param {Any[]} array 
 * @param {Number} start 
 * @param {Number} end 
 */
function quickSort(array, start, end) {
  if (start >= end) {
    return array;
  }
  
  let pIndex = partition(array, start, end);
  quickSort(array, start, pIndex - 1);
  quickSort(array, pIndex + 1, end);

  return array;
}

function sortArray(array) {
    return quickSort(array, 0, array.length - 1);
}