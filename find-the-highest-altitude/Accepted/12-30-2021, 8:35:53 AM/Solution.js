// https://leetcode.com/problems/find-the-highest-altitude

/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
  let max = 0;
  let sumAlt = 0;

  for (let alt of gain) {
    sumAlt += alt;
    if (sumAlt > max) {
      max = sumAlt;
    }
  }
  return max;
};