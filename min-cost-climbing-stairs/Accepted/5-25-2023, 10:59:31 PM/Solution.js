// https://leetcode.com/problems/min-cost-climbing-stairs

/**
 * @param {*} cost
 * @param {*} last
 * @param {*} memo
 * @returns
 */
function helper(cost, last, memo) {
  if (last === 1 || last === 0) return cost[last];

  if (memo.has(last)) {
    return memo.get(last);
  }

  const result =
    cost[last] +
    Math.min(helper(cost, last - 1, memo), helper(cost, last - 2, memo));

  memo.set(last, result);
  return result;
}

/**
 * @param {number[]} cost
 * @return {number}
 */
function minCostClimbingStairs(cost) {
  const last = cost.length - 1;
  const memo = new Map();

  return Math.min(helper(cost, last, memo), helper(cost, last - 1, memo));
}
