// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) 
{
  let pairs = 0;
    for (let i = 0; i < nums.length - 1; i++)
    {
        for (let j = i+1; j < nums.length; j++)
        {
         let x = nums[i] - nums[j];
            if(Math.abs(x) == k)
            {
                pairs++;
            }
        }
    }
    return pairs;  
};