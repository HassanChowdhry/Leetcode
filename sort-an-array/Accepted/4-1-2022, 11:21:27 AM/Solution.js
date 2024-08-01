// https://leetcode.com/problems/sort-an-array

/**
 *? Time O(n), Space O(n)
 * @param {Any[]} left 
 * @param {Any[]} right 
 * @param {Any[]} array
 * @returns {Any[]}
 */
function merge(left, right, array) {

  while (left.length > 0 && right.length > 0) {
    if (left[0] > right[0]) {

      let smallerNum = right.shift();
      array.push(smallerNum);
    
    } else {
      let smallerNum = left.shift();
      array.push(smallerNum);
    }

  }

  while (left.length > 0) {
    array.push(left.shift());
  }

  while (right.length > 0) {
    array.push(right.shift());
  }

  return array;
}

/**
 ** Time O(nlogn) , Space O(n)
 * @param {Any[]} array
 * @returns {Any[]}
 */
function sortArray(array) {
  let n = array.length; 

  if (n <= 1) {
    return array;
  }

  let mid = Math.floor(n / 2);
  let left = [];
  let right = [];

  for (let i = 0; i < mid; i++) {
    left.push(array.shift());
  }
  
  for (let j = mid; j < n; j++) {
    right.push(array.shift());
  }

  sortArray(left); 
  sortArray(right);
  merge(left, right, array);

  return array;
}
