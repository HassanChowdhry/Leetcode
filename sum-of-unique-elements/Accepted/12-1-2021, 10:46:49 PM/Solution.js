// https://leetcode.com/problems/sum-of-unique-elements

/**
 * @param {number[]} nums
 * @return {number}
 */
function sumOfUnique(nums) 
{
  let sum = 0;
        for (let i = 0; i < nums.length; i++)
        {
            let x = true;
            for (let j = 0; j < nums.length; j++)
            {
                if (i !== j)
                {
                   if (nums[i] === nums[j])
                     {
                       x = false;
                       break;
                     } 
                }  
            }      
             if (x === true)
             {
                sum += nums[i];
             }
            
        }
        return sum;
};