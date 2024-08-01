// https://leetcode.com/problems/number-of-good-pairs

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) 
{
     var goodPairs  = 0;
    for (var i = 0; i < nums.length - 1; i++)
    {
       for (var j = i + 1; j < nums.length; j++)
       {
         if (nums[i] == nums[j])
         {
             goodPairs++;
         }
         
       }
    }   
    return goodPairs; 
};