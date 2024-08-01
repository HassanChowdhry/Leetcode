// https://leetcode.com/problems/pascals-triangle-ii

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    let res = [[1]];
  if (rowIndex === 0) return res;

  for (let i = 1; i <= 33; i++) {
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
    if (i === rowIndex) return res[i];
  }

  return [];
};