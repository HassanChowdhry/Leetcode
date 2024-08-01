// https://leetcode.com/problems/robot-return-to-origin

/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
     let verticalPos = 0;
  let horizontalPos = 0;
  for (let c of moves) {
    if (c === 'U') {
      verticalPos++;
    }
    else if (c === 'D') {
      verticalPos--;
    }
    else if (c === 'R') {
      horizontalPos++;
    }
    else if (c === 'L') {
      horizontalPos--;
    }
  }
  if (verticalPos === 0 && horizontalPos === 0) {
    return true;
  }
  return false;
};