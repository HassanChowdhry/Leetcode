// https://leetcode.com/problems/fizz-buzz

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) 
{
    let s = [];
    for (let i = 1; i <= n; i++)
    {
        if (i % 3 === 0 && i % 5 === 0)
        {
           s.push("FizzBuzz");
        }
        else if (i % 3 === 0)
        {
            s.push("Fizz")
        }
        else if (i % 5 === 0)
        {
            s.push("Buzz")
        }
        else 
        {
            s.push(i.toString());
        }
    }
    return s;
    
    
};