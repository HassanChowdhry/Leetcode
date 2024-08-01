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
  stones = stones.sort((a, b) => a - b);
  let largest = stones[stones.length - 1];
  let secondLargest = stones[stones.length - 2];
  if (largest === secondLargest) {
    stones.pop();
    stones.pop();
  } else {
    largest -= secondLargest;
    stones.pop();
    stones.pop();
    stones.push(largest);
  }
  return lastStoneWeight(stones);
};