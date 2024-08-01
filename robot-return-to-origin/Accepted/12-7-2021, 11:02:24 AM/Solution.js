// https://leetcode.com/problems/robot-return-to-origin

/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
     let verticalPos = 0;
  let horizontalPos = 0;
  for (let c of moves) {
    switch (c) {
      case 'U':
        verticalPos++;
        break;
      case 'D':
        verticalPos--;
        break;
      case 'L':
        horizontalPos--;
        break;
      case 'R':
        horizontalPos++;
        break;
      default:
        return false;
    }
  }
  return (verticalPos === 0 && horizontalPos === 0);
}