// https://leetcode.com/problems/fizz-buzz

/**
 * @param {number} n
 * @return {string[]}
 */
function buzzHelper(n, counter, resultArray) {
  if (n < counter) {
    return resultArray;
  }

  let isDivisibleBy3 = counter % 3 === 0;
  let isDivisibleBy5 = counter % 5 === 0;

  if (isDivisibleBy3 && isDivisibleBy5) {
    resultArray.push('FizzBuzz');
  } else if (isDivisibleBy3) {
    resultArray.push('Fizz');
  } else if (isDivisibleBy5) {
    resultArray.push('Buzz');
  } else {
    resultArray.push(counter.toString());
  }

  return buzzHelper(n, counter + 1, resultArray);
}

function fizzBuzz(n) {
  return buzzHelper(n, 1, []);
}