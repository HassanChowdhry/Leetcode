// https://leetcode.com/problems/sqrtx

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
  if (x === 1 || x === 0) return x; // special case

  let half = x;
  let halfSqr = half * half;
  let prev;
  while (halfSqr > x) { // keeps half x untill halfsqr less than x and keeps track of prev half
    prev = half;
    half = Math.floor(half / 2); 
    halfSqr = half * half;
  }

  half = Math.floor((prev + half) / 2); // middle of the sqr numbers less than 'half' and 'prevHalf'
  halfSqr = half * half; // updates halfsqr

  while (half > 0) {
    if (halfSqr === x || (halfSqr < x && ((half + 1) * (half + 1) > x))) { // checks if 'x' is between range
      return half;
    }
    // subtracts or adds 1 to half depending on if halfsqr is larger or smaller than 'x'
    if (halfSqr > x) {
      half--;
      halfSqr = half * half;
    } else if (halfSqr < x) {
      half++;
      halfSqr = half * half;
    }
  }
  
  return x;
};