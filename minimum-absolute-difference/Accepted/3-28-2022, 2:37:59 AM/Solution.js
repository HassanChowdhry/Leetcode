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

  for (let i = 0; i < arr.length; i++) {

    for (let j = i + 1; j < arr.length; j++) {
      
      if (Math.abs(arr[i] - arr[j]) === minDiff) {
        res.push([arr[i], arr[j]]);

      } else if (Math.abs(arr[i] - arr[j]) > minDiff) {
        break;
        
      } else {
        res = [[arr[i], arr[j]]];
        minDiff = Math.abs(arr[i] - arr[j]);
      }
    }
  }

  return res;
}
