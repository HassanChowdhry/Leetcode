// https://leetcode.com/problems/number-of-good-pairs

function numIdenticalPairs(nums: number[]): number {

    let goodPairs  = 0;
    for (let i = 0; i < nums.length - 1; i++)
    {
       for (let j = i + 1; j < nums.length; j++)
       {
         if (nums[i] == nums[j])
         {
             goodPairs++;
         }
         
       }
    }   
    return goodPairs; 
};