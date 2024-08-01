// https://leetcode.com/problems/baseball-game

/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
  let record = [];

  for (let ops of operations) {
    opReader(ops, record);
  }

  return record.reduce((a, b) => a + b, 0)
};

function opReader(ops, record) {
  if (ops === "C") {
    record.pop();
  } else if (ops === "D") {
    record.push(record[record.length -1] * 2);
  } else if (ops === "+") {
    record.push(record[record.length -1] * 1 + record[record.length -2] * 1);
  } else {
    record.push(ops * 1);
  }
}