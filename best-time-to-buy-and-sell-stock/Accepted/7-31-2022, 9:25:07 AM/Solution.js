// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let buyDay = 0;
  let profit = prices[1] - prices[buyDay];

  for (let i = 1; i < prices.length; i++) {
    let currProfit = prices[i] - prices[buyDay];
    
    if (profit < currProfit) {
      profit = currProfit;
    }

    if (prices[buyDay] > prices[i]) {
      buyDay = i;
    }
  }

  return (profit > 0 ? profit : 0);

};