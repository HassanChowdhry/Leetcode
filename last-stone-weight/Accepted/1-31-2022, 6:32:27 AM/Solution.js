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
  stones = stones.sort((a, b) => b - a);
  let largest = stones[0];
  let secondLargest = stones[1];
  if (largest === secondLargest) {
    stones.shift();
    stones.shift();
  } else {
    largest -= secondLargest;
    stones.shift();
    stones.shift();
    stones.push(largest);
  }
  return lastStoneWeight(stones);
};