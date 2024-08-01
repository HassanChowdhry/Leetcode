// https://leetcode.com/problems/roman-to-integer

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
      let romanMap = new Map();
  let num = 0;

  romanMap.set('M', 1000);
  romanMap.set('D', 500);
  romanMap.set('C', 100);
  romanMap.set('L', 50);
  romanMap.set('X', 10);
  romanMap.set('V', 5);
  romanMap.set('I', 1);
  
  for (let i = 0; i < s.length; i++) {
    let currentRoman = romanMap.get(s[i]);
    let nextRoman = romanMap.get(s[i + 1]);
    
    if (currentRoman < nextRoman) {
      num -= currentRoman;
    } else {
      num += currentRoman;
    }
  }

  return num;
};