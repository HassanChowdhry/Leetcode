// https://leetcode.com/problems/sqrtx

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
 if (x === 1 || x === 0) return x;
  
  let half = x;
  let halfSqr = half * half;
  let prev;
  while (halfSqr > x) {
    prev = half;
    half = Math.floor(half / 2);
    halfSqr = half * half;
  }

  half = Math.floor((prev + half) / 2);
  halfSqr = half * half;

  while (true) {
    if (halfSqr === x || (halfSqr < x && ((half + 1) * (half + 1) > x))) {
      return half;
    }
    if (halfSqr > x) {
      half--;
      halfSqr = half * half;
    } else if (halfSqr < x) {
      half++;
      halfSqr = half * half;
    }
  }
  
};