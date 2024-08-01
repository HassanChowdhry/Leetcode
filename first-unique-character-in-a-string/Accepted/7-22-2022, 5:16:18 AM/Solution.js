// https://leetcode.com/problems/first-unique-character-in-a-string

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(str) {
     let strMap = new Map();
  
  for (let c of str) {
    if (strMap.has(c)) {
      strMap.set(c, strMap.get(c) + 1);    
    } else {
      strMap.set(c, 1);
    }
  }

  for (let [key, value] of strMap.entries()) {
    if (value === 1) {
      return str.indexOf(key);
    }
  }

  return -1;  
};