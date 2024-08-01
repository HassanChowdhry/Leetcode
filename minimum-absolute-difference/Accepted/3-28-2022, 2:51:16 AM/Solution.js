// https://leetcode.com/problems/minimum-absolute-difference

/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
arr = arr.sort((a, b) => a - b);
  if (arr.length === 2) {
    return [arr];  
  }

  let res = [];
  let minDiff = Math.abs(arr[0] - arr[1]);

  for (let i = 1; i < arr.length; i++) {

    if (Math.abs(arr[i - 1] - arr[i]) < minDiff) {

      res = [[arr[i - 1], arr[i]]];
      minDiff = Math.abs(arr[i - 1] - arr[i]);
    
    } else if (Math.abs(arr[i - 1] - arr[i]) === minDiff) {

      res.push([arr[i - 1], arr[i]]);
    }
  }

  return res;
}