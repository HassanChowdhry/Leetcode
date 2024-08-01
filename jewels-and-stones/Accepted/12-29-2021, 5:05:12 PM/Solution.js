// https://leetcode.com/problems/jewels-and-stones

/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    
     let jewelSet = new Set();
  let jewelCount = 0;

  for (let jewel of jewels) {
    jewelSet.add(jewel);
  }

  for (let stone of stones) {
    if (jewelSet.has(stone)) {
      jewelCount++;
    }
  }
  return jewelCount;
};