// https://leetcode.com/problems/pascals-triangle

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let res = [[1]];

  for (let i = 1; i < numRows; i++) {
    let row = [1];

    for (let j = 1; j <= i; j++) {
      if (i === j) {
        row.push(1);
        break;
      }
      let num = res[i - 1][j - 1] + res[i - 1][j];
      row.push(num);

    }
    res.push(row);
  }

  return res;
};