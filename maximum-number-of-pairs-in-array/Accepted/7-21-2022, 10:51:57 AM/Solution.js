// https://leetcode.com/problems/maximum-number-of-pairs-in-array

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    let set = new Set();
    let pairCounter = 0;
    
    for (let n of nums) {
        if (set.has(n)) {
            pairCounter++;
            set.delete(n);
        } else {
            set.add(n)
        }
    }
    
    return [pairCounter, set.size];
};