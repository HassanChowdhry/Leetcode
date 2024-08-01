// https://leetcode.com/problems/find-the-highest-altitude

/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
   let highestAlt = 0;
  let currentAlt = 0;

  gain.forEach((alt) => {
    currentAlt += alt;
    highestAlt = Math.max(currentAlt, highestAlt);
  });
   
  return highestAlt;
};