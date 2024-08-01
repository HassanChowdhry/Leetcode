// https://leetcode.com/problems/intersection-of-two-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let resultSet = new Set();   
    let set1 = new Set();
    
    for (let num of nums1)
        set1.add(num);
     
    for (let num of nums2)
        if (set1.has(num))
            resultSet.add(num);

    let result = [];
    for (let num of resultSet.values())
        result.push(num);

    return result;
};