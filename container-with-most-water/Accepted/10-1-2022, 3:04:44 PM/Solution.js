// https://leetcode.com/problems/container-with-most-water

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
      let mxArea = 0;
  let left = 0;
  let right = height.length - 1;
  let len = height.length - 1;

  while (left < right) {
    let area;
    if (height[left] < height[right]) {
      area = height[left] * len;
      left += 1;
    
    } else {
      area = height[right] * len;
      right -= 1;
    }
    
    mxArea = (mxArea < area ? area : mxArea); 
    len -= 1;
  }

  return mxArea;
};