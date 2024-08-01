// https://leetcode.com/problems/fizz-buzz

/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) 
{
  let s = [];
  for (let i = 1; i <= n; i++) {
    let isDivisibleBy3 = i % 3 === 0;
    let isDivisibleBy5 = i % 5 === 0;
    if (isDivisibleBy3 && isDivisibleBy5) {
      s.push('FizzBuzz');
    } else if (isDivisibleBy3) {
      s.push('Fizz');
    } else if (isDivisibleBy5) {
      s.push('Buzz');
    } else {
      s.push(i.toString());
    }
  }
  return s;
};