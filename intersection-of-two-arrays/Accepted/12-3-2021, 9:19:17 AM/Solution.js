// https://leetcode.com/problems/intersection-of-two-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let finalNum = [];   
    let uniqueNum = new Set();
    
    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            if (nums1[i] === nums2[j])
            uniqueNum.add(nums1[i]);
        }
     }
     
     for (let number of uniqueNum){
         finalNum.push(number);
     }
     return finalNum
};