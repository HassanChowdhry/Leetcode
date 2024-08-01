// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num)
{
    let steps = 0;
       if (num == 0)
       {
           return 0;
       }
       while (num > 0)
       {
           if ( num % 2 == 0)
           {
              num = parseInt(num/2);
           }
           else num -= 1;
           steps++;
       }
       return steps 
};