// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

/**
 * 
 * @param {number[][]} mat 
 * @param {number} k
 * @returns {number[]} 
 */
// Time O(n), Space O(n)
function kWeakestRows2(mat, k) {
  let pQueue = new PriorityQueue((a, b) => (a[1] === b[1] ? a[0] < b[0] : a[1] < b[1]));
  let result = [];

  for (let i = 0; i < mat.length; i++) {
    let sum = 0;
    for (let j = 0; j < mat[i].length; j++) {
      if (mat[i][j] === 0) {
        break;
      }
      sum++;
    }
    pQueue.push([i, sum]);
  }

  while (k > 0) {
    result.push(pQueue.pop()[0]);
    k--;
  }

  return result;
}

/**
 ** Time O(logN), Space O(1)
 * @param {Any[]} array 
 * @returns 
 */
function binSearch(array) {
  
  let start = 0;
  let end = array.length - 1;
  let soldiers = 0;

  while (start <= end) {
    let middle = Math.floor((start + end) / 2);

    if (array[middle] === 1) {
      soldiers = middle + 1;
      start = middle + 1;

    } else {
      end = middle - 1;   
    }

  }
  return soldiers;
}

/**
 ** Time O(nlogn), Space O(n)
 * @param {number[][]} mat 
 * @param {number} k
 * @returns {number[]} 
 */
function kWeakestRows(mat, k) {
  let res = [];
  
  for (let i = 0; i < mat.length; i++) {
    res.push([i, binSearch(mat[i])]);
  }

  res = res
    .sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]))
    .slice(0, k)
    .map((item) => item[0]);

  return res;
}
