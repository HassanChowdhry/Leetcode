// https://leetcode.com/problems/last-stone-weight

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    if (stones.length === 1) {
    return stones[0];
  }
  if (stones.length === 0) {
    return 0;
  }
  stones.sort((a, b) => a - b);

  let largest = stones.pop();
  let secondLargest = stones.pop();
  if (largest !== secondLargest) {
    largest -= secondLargest;
    stones.push(largest);
  }
  return lastStoneWeight(stones);
};