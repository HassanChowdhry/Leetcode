// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix


const top = 0;
const parent = (i) => ((i + 1) >>> 1) - 1;
const left = (i) => (i << 1) + 1;
const right = (i) => (i + 1) << 1;

class PriorityQueue {
  constructor(comparator = (a, b) => a > b) {
    this._heap = [];
    this._comparator = comparator;
  }

  size() {
    return this._heap.length;
  }

  isEmpty() {
    return this.size() === 0;
  }

  peek() {
    return this._heap[top];
  }

  push(...values) {
    values.forEach((value) => {
      this._heap.push(value);
      this._siftUp();
    });
    return this.size();
  }

  pop() {
    const poppedValue = this.peek();
    const bottom = this.size() - 1;
    if (bottom > top) {
      this._swap(top, bottom);
    }
    this._heap.pop();
    this._siftDown();
    return poppedValue;
  }

  replace(value) {
    const replacedValue = this.peek();
    this._heap[top] = value;
    this._siftDown();
    return replacedValue;
  }

  _greater(i, j) {
    return this._comparator(this._heap[i], this._heap[j]);
  }

  _swap(i, j) {
    [this._heap[i], this._heap[j]] = [this._heap[j], this._heap[i]];
  }

  _siftUp() {
    let node = this.size() - 1;
    while (node > top && this._greater(node, parent(node))) {
      this._swap(node, parent(node));
      node = parent(node);
    }
  }

  _siftDown() {
    let node = top;
    while (
      (left(node) < this.size() && this._greater(left(node), node))
      || (right(node) < this.size() && this._greater(right(node), node))
    ) {
      let maxChild = (right(node) < this.size() && this._greater(right(node), left(node))) ? right(node) : left(node);
      this._swap(node, maxChild);
      node = maxChild;
    }
  }
}

module.exports = PriorityQueue;

/**
 ** Time O(logN), Space O(1)
 * @param {Any[]} array 
 * @returns 
 */
function binSearch(array) {
  
  let start = 0;
  let end = array.length - 1;
  let soldiers = 0;

  while (start <= end) {
    let middle = Math.floor((start + end) / 2);

    if (array[middle] === 1) {
      soldiers = middle + 1;
      start = middle + 1;

    } else {
      end = middle - 1;   
    }

  }
  return soldiers;
}

/**
 ** Time O(nlogn), Space O(n)
 * @param {number[][]} mat 
 * @param {number} k
 * @returns {number[]} 
 */
function kWeakestRows(mat, k) {
  let pQueue = new PriorityQueue((a, b) => (a[1] === b[1] ? a[0] < b[0] : a[1] < b[1]));
  let res = [];
  
  for (let i = 0; i < mat.length; i++) {
    pQueue.push([i, binSearch(mat[i])]);
  }

  while (k > 0) {
    res.push(pQueue.pop()[0]);
    k--;
  }

  return res;
}
