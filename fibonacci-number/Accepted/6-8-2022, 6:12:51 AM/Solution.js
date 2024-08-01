// https://leetcode.com/problems/fibonacci-number

function fib(n) {
  if (n === 0 || n === 1) {
    return n;
  }
  
  let array = [0, 1];
  for (let i = 2; i <= n; i++) {
    array[i] = array[i - 2] + array[i - 1];
  }
  return array.pop();
}