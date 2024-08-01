// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const smallerNumbersThanCurrent = (nums) => (
  nums.map((num1, i) => (
    nums.reduce((count, num2, j) => {
      if (num1 > num2 && i !== j) {
        count++;
      }
      return count++;
    }, 0)
  ))
);