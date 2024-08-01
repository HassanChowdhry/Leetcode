// https://leetcode.com/problems/fibonacci-number

const map = new Map();
map.set(0, 0)
map.set(1, 1)

var fib = function(n) {
    if (n <= 1) return map.get(n)
    const result = fib(n-1) + fib(n-2)
    map.set(n, result)
    return map.get(n)
};