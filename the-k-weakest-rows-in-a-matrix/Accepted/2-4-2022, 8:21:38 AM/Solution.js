// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
    let result = [];

  for (let i = 0; i < mat.length; i++) {
    let sum = 0;
    for (let j = 0; j < mat[0].length; j++) {
      sum += mat[i][j];
    }
    result.push([i, sum]);
  }

  result.sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]));
  result = result.slice(0, k);
  result = result.map((item) => item[0]);

  return result;
};