// https://leetcode.com/problems/remove-duplicates-from-sorted-array

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let prev;
    let curr;
    for (let i = 1; i < nums.length; i++) {
        prev = nums[i - 1]
        curr = nums[i];
        
        if (prev === curr) {
            nums.splice(i, 1);
            i--;
        }
    }
};