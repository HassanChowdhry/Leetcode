// https://leetcode.com/problems/last-stone-weight

class TwoLargest {

  /**
   * 
   * @param {number} largest 
   * @param {number} secondLargest 
   * @param {number} maxIndex
   * @param {number} secondMaxIndex
   */

  constructor(largest, secondLargest, maxIndex, secondMaxIndex) {
    this.largest = largest;
    this.secondLargest = secondLargest;
    this.maxIndex = maxIndex;
    this.secondMaxIndex = secondMaxIndex;
  }

}

/**
 * 
 * @param {number[]} stones 
 * @returns {TwoLargest}
 */
function findTwoLargest(stones) {
  let largest = 0;
  let secondLargest = 0;
  let maxIndex = 0;
  let secondMaxIndex = 0;

  for (let i = 0; i < stones.length; i++) {

    if (largest <= stones[i]) {
      maxIndex = i;
      secondMaxIndex = stones.indexOf(largest);

      let tmp = largest;
      largest = stones[i];
      secondLargest = tmp;

    } else if (secondLargest <= stones[i]) {
      secondLargest = stones[i];
      secondMaxIndex = i;
    }

  }

  // TODO: remove the bad bois in here
  return new TwoLargest(largest, secondLargest, maxIndex, secondMaxIndex);
}
/**
 * @param {number[]} stones
 * @return {number}
 */
// Time O(n), Space O(1) 
function lastStoneWeight(stones) {
  if (stones.length === 1) {
    return stones[0];
  }
  if (stones.length === 0) {
    return 0;
  }

  let findLargest = findTwoLargest(stones);

  let { largest } = findLargest;
  let { secondLargest } = findLargest;
  let { maxIndex } = findLargest;
  let { secondMaxIndex } = findLargest;
  
  if (largest === secondLargest) {
    
    stones.splice(maxIndex, 1);

    
    stones.splice(secondMaxIndex, 1);
  
  } else {
    stones[maxIndex] = largest - secondLargest;

    stones.splice(secondMaxIndex, 1);
  
  }

  return lastStoneWeight(stones);
}