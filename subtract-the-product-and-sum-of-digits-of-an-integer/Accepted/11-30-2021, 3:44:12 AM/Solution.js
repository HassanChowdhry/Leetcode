// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) 
{
    var product = 1;
    var sum = 0;

    if ( n == 0 )
    {
       return 0;
    }
    
    while (n > 0)
    {
        let digit = n % 10
        product *= digit;
        sum += digit;
        n = parseInt(n/10);

    }

    return product - sum; 
};