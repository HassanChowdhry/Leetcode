// https://leetcode.com/problems/find-lucky-integer-in-an-array

/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    let map = new Map();
  let luckyNum = -1;

  arr.forEach((num) => {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    
    } else map.set(num, 1);
  });
  
  for (let [key, value] of map) {
    if (key === value) {
      luckyNum = Math.max(luckyNum, key);
    }
  }

  return luckyNum;
};