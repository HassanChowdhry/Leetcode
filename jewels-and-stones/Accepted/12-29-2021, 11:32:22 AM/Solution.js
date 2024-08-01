// https://leetcode.com/problems/jewels-and-stones

/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    return stones.split('').reduce((acc, c) => {
    if (jewels.includes(c)) {
      acc++;
    }
    return acc;
  }, 0);
};