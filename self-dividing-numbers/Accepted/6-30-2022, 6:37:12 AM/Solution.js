// https://leetcode.com/problems/self-dividing-numbers

/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    let resArray = [];

  while (left <= right) {
    let leftStr = left.toString();
    let isSelfDiv = true;

    for (let i = 0; i < leftStr.length; i++) {
      if (left % leftStr.charAt(i) !== 0) {
        isSelfDiv = false;
        break;
      }
    }

    if (isSelfDiv) {
      resArray.push(left);
    }
    
    left++;
  }

  return resArray;
}