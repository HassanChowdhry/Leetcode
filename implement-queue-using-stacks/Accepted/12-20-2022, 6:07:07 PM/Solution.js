// https://leetcode.com/problems/implement-queue-using-stacks

// var MyQueue = function() {
//   let stack = [];
// };

class MyQueue {
  constructor() {
    this.stack = [];
  }

  push(x) {
    this.stack.push([x]);
  }

  pop() {
    return this.stack.shift();
  }

  peek() {
    return this.stack[0];
  }

  empty() {
    return this.stack.length === 0;
  }
}
// /** 
//  * @param {number} x
//  * @return {void}
//  */
// MyQueue.prototype.push = function(x) {
//     let inner = [x];
//     this.stack.push(inner);
// };

// /**
//  * @return {number}
//  */
// MyQueue.prototype.pop = function() {
//     return this.stack.pop();
// };

// /**
//  * @return {number}
//  */
// MyQueue.prototype.peek = function() {
//     return this.stack[0];
// };

// /**
//  * @return {boolean}
//  */
// MyQueue.prototype.empty = function() {
//     return this.stack.length === 0;
// };

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */