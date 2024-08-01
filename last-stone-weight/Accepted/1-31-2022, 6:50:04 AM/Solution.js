// https://leetcode.com/problems/last-stone-weight

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    
  while (stones.length > 1) {
    stones.sort((a, b) => a - b);

    let largest = stones.pop();
    let secondLargest = stones.pop();

    if (largest !== secondLargest) {
      stones.push(largest - secondLargest);
    }
  }
  if (stones.length === 1) {
    return stones[0];
  }
  return 0;
};