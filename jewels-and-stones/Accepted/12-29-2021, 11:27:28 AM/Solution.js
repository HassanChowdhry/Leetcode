// https://leetcode.com/problems/jewels-and-stones

/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
     let numJewels = 0;

  for (let c of stones) {

    if (jewels.indexOf(c) !== -1) {
      numJewels++;
    }
  }
  return numJewels;
};